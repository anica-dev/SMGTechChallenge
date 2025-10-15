from fastapi import FastAPI, Query
from typing import List, Optional
from app.scraping import scrape_website

app = FastAPI()

@app.get("/")
async def root(group: Optional[List[str]] = Query(None), exclude: Optional[List[str]] = Query(None)):
    all_brands = scrape_website("https://swissmarketplace.group/")
    filtered_brands = []
    if group:
        for brand in all_brands:
            if brand.name.lower().replace(" ", "") in group:
                filtered_brands.append(brand)
        return filtered_brands
    elif exclude:
        for brand in all_brands:
            if brand.name.lower().replace(" ", "") not in exclude:
                filtered_brands.append(brand)
        return filtered_brands
    return all_brands



