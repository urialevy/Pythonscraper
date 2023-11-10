from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()


@app.get("/{asin}")
def get_data(asin: str):
    session = requests.Session()
    session.headers.update({
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    })
    resp = session.get("https://google.com")
    soup = BeautifulSoup(resp.text, "html.parser")
    data = {
        "asin": asin,
        "name": soup.select_one("h1#title").text,
        "price": soup.select_one("span.a-offspring").text
    }
    return{"results":data}