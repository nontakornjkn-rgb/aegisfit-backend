from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path

# สร้าง instance ของ FastAPI
app = FastAPI(
    title="AEGIS FIT API",
    description="AI-powered fitness application backend built with FastAPI, Supabase, and OpenAI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

# กำหนดพาธไปยังโฟลเดอร์ static
STATIC_DIR = Path("static")

# 1. Route สำหรับ Landing Page (Root URL)
# **สำคัญ:** เราจะใช้ HTMLResponse เพื่ออ่านไฟล์ index.html โดยตรง
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root():
    """
    Serves the static index.html landing page at the root URL.
    """
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse("<h1>Error: index.html not found in static folder.</h1>", status_code=500)
    
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# 2. Route สำหรับ API (ตัวอย่าง)
@app.get("/api/status", tags=["default"])
def get_status():
    """
    Get Status
    """
    return {"status": "ok", "message": "AEGIS FIT API is running."}

# 3. Route สำหรับ Redirect /docs (เพื่อให้เข้าถึงได้ง่าย)
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return RedirectResponse(url=app.docs_url)
