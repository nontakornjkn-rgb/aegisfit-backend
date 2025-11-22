from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

# สร้าง instance ของ FastAPI
app = FastAPI(
    title="AEGIS FIT API",
    description="AI-powered fitness application backend built with FastAPI, Supabase, and OpenAI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

# 1. Mount StaticFiles สำหรับ Landing Page
# **สำคัญ:** ต้อง Mount ก่อน Route อื่นๆ ทั้งหมด เพื่อให้ "/" ถูกจับโดย StaticFiles
# directory="static" คือโฟลเดอร์ที่เก็บ index.html
# html=True คือการบอกให้ StaticFiles เสิร์ฟ index.html เมื่อเข้าถึง /
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# 2. Route สำหรับ API (ตัวอย่าง)
@app.get("/api/status", tags=["default"])
def get_status():
    """
    Read Status
    """
    return {"status": "ok", "message": "AEGIS FIT API is running."}

# 3. Route พิเศษสำหรับ Redirect /docs
# เนื่องจากเรา Mount StaticFiles ที่ "/" ทำให้ /docs ถูก StaticFiles จับไปด้วย
# เราจึงต้องเพิ่ม Route นี้เพื่อบังคับให้ /docs แสดงหน้าเอกสาร API
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return RedirectResponse(url="/docs")

# 4. Route พิเศษสำหรับ Redirect /redoc (ถ้าต้องการ)
# @app.get("/redoc", include_in_schema=False)
# async def redoc_html():
#     return RedirectResponse(url="/redoc")

# หมายเหตุ: หากต้องการเพิ่ม Route API อื่นๆ ให้เพิ่มต่อจากนี้
