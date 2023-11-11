from requests_html import HTMLSession

class Scraper():
    
    def __init__(self, url,tag,s) -> None:
        self.url = url
        self.tag = tag
        self.s = s

    def scrape_data(self, url, tag, s):
        url = f"https://quotes.toscrape.com/tag/{tag}"
        r = s.get(url)
        qlist = []
        quotes = r.html.find('div.quote')
     
        for q in quotes:
            item = {
                "text": q.find('span.text', first=True).text.strip(),
                "author": q.find('small.author', first=True).text.strip()
             }
            qlist.append(item)
        return qlist

humor_quotes = Scraper("https://quotes.toscrape.com/tag/", "humor", HTMLSession())

print(humor_quotes.scrape_data("https://quotes.toscrape.com/tag/", "humor", HTMLSession()))