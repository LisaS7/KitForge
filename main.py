import logging

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import KITS_DIR, LOG_FILE, PROJECT_ROOT
from src.store import load_all

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[logging.FileHandler(LOG_FILE)],
)

app = FastAPI()
app.mount("/static", StaticFiles(directory=PROJECT_ROOT / "src" / "static"), name="static")
templates = Jinja2Templates(directory=PROJECT_ROOT / "src" / "templates")


@app.get("/", response_class=HTMLResponse)
async def kit_list(request: Request):
    kits = load_all(KITS_DIR)
    return templates.TemplateResponse(request, "kit_list.html", {"kits": kits})
