FROM python:3.11-slim

WORKDIR /lagunascraper

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["scrapy", "crawl", "books", "-o", "output/books.csv"]
