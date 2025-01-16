from fastapi import FastAPI # required for launch
from fastapi.responses import RedirectResponse, HTMLResponse # the response page
from fastapi.templating import Jinja2Templates # for link with directory "templates"
from fastapi.requests import Request # response
from fastapi.staticfiles import StaticFiles # for transfer styles on pages from "static/css/style.css"


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return RedirectResponse(url = "/index_html/")

@app.get("/index_html/", response_class=HTMLResponse)
async def main_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.mount("/static", StaticFiles(directory="static"), name="static") # connecting the display of styles