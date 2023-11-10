from typing import Union
from typing import  List
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

def create_url(month:str,day:int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def retrieve_page(url:str) -> BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def events_of_the_day(month:str,day:int) -> List[str]:
    url = create_url(month, day)
    page = retrieve_page(url)
    raw_events = page.find_all(class_ = "event")
    events = [event.text for event in raw_events]
    return events

