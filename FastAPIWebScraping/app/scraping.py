from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel
from typing import List

class ourBrands(BaseModel):
    name: str
    links: List[str]

def scrape_website(url):
    brands_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        parent_divs = soup.find_all('div', class_='uagb-container-inner-blocks-wrap')
        our_brands_div = None
        for d in parent_divs:
            if "Meet our Brands" in d.get_text():
                our_brands_div = d
        target_divs = our_brands_div.find_all('div', class_='wp-block-uagb-container')[1:]
        for div in target_divs:
            h3 = div.find('h3')
            links = div.find_all('a')
            urls = []
            for l in links:
                url = l.get('href')
                urls.append(url)
            brands = ourBrands(name=h3.text, links=urls)
            brands_list.append(brands)
        return brands_list
    else:
        return {"error": f"Request failed, status code: {response.status_code}"}

if __name__ == '__main__':
    print(scrape_website("https://swissmarketplace.group/"))
