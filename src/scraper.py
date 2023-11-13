from requests_html import HTMLSession

class Scraper():

    def __init__(self):
        self.quote_url = "https://quotes.toscrape.com/tag/"
        self.session = HTMLSession()

    def scrape_data(self, tag):
        url = f"{self.quote_url}{tag}"
        r = self.session.get(url)
        qlist = []
        quotes = r.html.find('div.quote')

        for q in quotes:
            item = {
                "text": q.find('span.text', first=True).text.strip(),
                "author": q.find('small.author', first=True).text.strip()
             }
            qlist.append(item)
        return qlist
    
print("testing branch")