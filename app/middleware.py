from __future__ import annotations

import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.contextvars import bind_contextvars, clear_contextvars


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Clear contextvars để tránh rò rỉ dữ liệu giữa các request
        clear_contextvars()

        # 2. Lấy x-request-id từ headers, nếu không có thì tự tạo mới theo định dạng req-<8-char-hex>
        header_id = request.headers.get("x-request-id")
        if header_id:
            correlation_id = header_id
        else:
            # Tạo UUID4 ngẫu nhiên, lấy 8 ký tự đầu tiên của chuỗi hex
            random_hex = uuid.uuid4().hex[:8]
            correlation_id = f"req-{random_hex}"
        
        # 3. Gắn correlation_id vào structlog contextvars để tất cả các dòng log sinh ra đều có trường này
        bind_contextvars(correlation_id=correlation_id)
        
        request.state.correlation_id = correlation_id
        
        # Ghi nhận thời gian bắt đầu xử lý request
        start = time.perf_counter()
        
        # Chuyển request đến endpoint xử lý
        response = await call_next(request)
        
        # Tính toán thời gian xử lý (đổi ra mili-giây ms)
        process_time_ms = (time.perf_counter() - start) * 1000
        
        # 4. Trả correlation_id và processing time về trong response headers
        response.headers["x-request-id"] = correlation_id
        response.headers["x-response-time-ms"] = f"{process_time_ms:.2f}"
        
        return response
