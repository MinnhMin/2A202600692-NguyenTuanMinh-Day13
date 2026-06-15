import os
from dotenv import load_dotenv
from langfuse import get_client  

# 1. Nạp biến môi trường từ .env
load_dotenv()

print("--- ĐANG KIỂM TRA THÔNG TIN KẾT NỐI (V3) ---")
print("Host:", os.getenv("LANGFUSE_HOST") or os.getenv("LANGFUSE_BASE_URL"))
print("Public Key:", os.getenv("LANGFUSE_PUBLIC_KEY"))

# 2. Khởi tạo client v3 và check auth
try:
    # Gọi get_client() để khởi tạo theo chuẩn v3
    langfuse = get_client()
    
    if langfuse.auth_check():
        print("\n[SUCCESS] Ket noi va xac thuc voi Cloud Langfuse THANH CONG!")
    else:
        print("\n[FAILED] Xac thuc THAT BAI! Cap Key hoac URL Host dang bi sai lech.")
except Exception as e:
    print(f"\n[ERROR] Loi khi goi auth_check: {str(e)}")