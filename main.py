from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# สร้าง instance ของ FastAPI
app = FastAPI(
    title="AEGIS FIT API",
    version="1.0.0",
    description="AI-powered fitness application backend built with FastAPI, Supabase, and OpenAI."
)

# 1. Mount StaticFiles (สำคัญ: ต้องอยู่ก่อน Route อื่นๆ)
# โค้ดนี้จะทำให้ไฟล์ index.html ในโฟลเดอร์ static ถูกเสิร์ฟเมื่อเข้าถึง Root Path ("/")
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# 2. Route หลัก (จะถูกเรียกก็ต่อเมื่อ StaticFiles ไม่พบไฟล์ที่ต้องการ)
# เนื่องจากเรามี index.html อยู่แล้ว Route นี้จะไม่ถูกเรียกเมื่อเข้าถึง "/"
# แต่จะยังคงทำงานเมื่อเข้าถึง /api/status
@app.get("/api/status")
def read_status():
    return {"name": "AEGIS FIT API", "version": "1.0.0", "status": "running"}

# 3. Route อื่นๆ ของ API (เช่น /docs, /openapi.json, ฯลฯ)
# ... คุณสามารถเพิ่ม API Endpoints อื่นๆ ของคุณได้ที่นี่ ...
