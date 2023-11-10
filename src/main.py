from typing import Union
from fastapi import FastAPI
from scraper import Scraper
app = FastAPI()
quotes = Scraper()

quotes.scrraperdata("humor")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{cat}")
async def read_item(cat):
    return quotes.scrraperdata(cat)