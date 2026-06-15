# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: [Điền tên nhóm của bạn vào đây nếu có]
- [REPO_URL]: [Điền link git của bạn vào đây]
- [MEMBERS]:
  - Member A: Nguyen Tuan Minh | Role: Logging & PII
  - Member B: [Tên thành viên] | Role: Tracing & Enrichment
  - Member C: [Tên thành viên] | Role: SLO & Alerts
  - Member D: [Tên thành viên] | Role: Load Test & Dashboard
  - Member E: [Tên thành viên] | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 12
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: screenshots/terminal_logs.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: screenshots/terminal_logs.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: screenshots/trace_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: Luồng chạy hiển thị rõ ràng sự phân tách giữa các RAG span và LLM span. Quá trình bóc tách thực tế cho thấy các khoảng thời gian sinh token được log đầy đủ thông qua Langfuse SDK.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: screenshots/image_ac5310.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 0ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.00 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: screenshots/image_ac4ca4.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: tool_fail & rag_slow
- [SYMPTOMS_OBSERVED]: Hệ thống dồn dập trả về lỗi 500 Internal Server Error đối với các request POST /chat. Trên giao diện giám sát, tỷ lệ lỗi vọt lên cao.
- [ROOT_CAUSE_PROVED_BY]: Log hệ thống in rõ lỗi "error_type": "RuntimeError" | "detail": "Vector store timeout" ứng với correlation_id: req-521f76e3 vào mốc thời gian 2026-06-15.
- [FIX_ACTION]: Áp dụng quy trình kiểm tra theo tài liệu hướng dẫn vận hành Runbook: rà soát các trace chậm nhất, khoanh vùng lỗi liên quan đến LLM/Tool, cô lập tool lỗi và cấu hình hạ kích thước prompt hoặc sử dụng model dự phòng.
- [PREVENTIVE_MEASURE]: Triển khai giám sát liên tục bằng các rule cảnh báo tự động trong config/alert_rules.yaml và tối ưu hóa bộ nhớ đệm prompt (prompt cache) để tránh quá tải hệ thống.

---

## 5. Individual Contributions & Evidence

### Nguyen Tuan Minh
- [TASKS_COMPLETED]: Cấu hình FastAPI, tích hợp Langfuse Tracing SDK v3, thiết kế hoàn chỉnh hệ thống lưới 6-panel Dashboard, viết file luật cảnh báo config/alert_rules.yaml và chạy thử nghiệm thành công các kịch bản sự cố.
- [EVIDENCE_LINK]: [Điền link commit chứa file alert_rules.yaml của bạn vào đây]

### [MEMBER_B_NAME]
- [TASKS_COMPLETED]: Hỗ trợ xây dựng cấu trúc thư mục, chuẩn hóa dữ liệu đầu vào sample_queries.jsonl để load test.
- [EVIDENCE_LINK]: [Link commit]

### [MEMBER_C_NAME]
- [TASKS_COMPLETED]: Soạn thảo tài liệu vận hành và hướng dẫn xử lý sự cố (Runbooks) trong docs/alerts.md.
- [EVIDENCE_LINK]: [Link commit]

### [MEMBER_D_NAME]
- [TASKS_COMPLETED]: Chạy file script load_test.py để sinh tải dữ liệu mẫu lên hệ thống Cloud.
- [EVIDENCE_LINK]: [Link commit]

### [MEMBER_E_NAME]
- [TASKS_COMPLETED]: Thu thập hình ảnh minh chứng và đóng gói tài liệu báo cáo hoàn chỉnh.
- [EVIDENCE_LINK]: [Link commit]

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)