from typing import Union
from fastapi import FastAPI, Request
from scraper import Scraper
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
quotes = Scraper()

templates = Jinja2Templates(directory="templates")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/{cat}")
async def read_quotes(cat):
    return quotes.scrape_data(cat)

@app.get("/scrape/{scraper_keyword}", response_class=HTMLResponse)
def read_item(request: Request, scraper_keyword: str):
    scraped_quotes = quotes.scrape_data(scraper_keyword)
    for scraped_quote in scraped_quotes:
        print(scraped_quote)
    return templates.TemplateResponse(
        "item.html", {"request": request, "quotes_list": scraped_quotes})

