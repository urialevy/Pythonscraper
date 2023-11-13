from typing import Union
from fastapi import FastAPI, Request
from scraper import Scraper
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
quotes = Scraper()

quotes.scrape_data("humor")

templates = Jinja2Templates(directory="templates")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/{cat}")
async def read_quotes(cat):
    return quotes.scrape_data(cat)

@app.get("/")
def read_item(request: Request, author: str, quote: str):
    return templates.TemplateResponse("/item.html", {"request": request, "author": author, "quote": quote})

