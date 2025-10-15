import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://laguna.rs/s_laguna_knjige_spisak_naslova.html"]

    def parse(self, response):
        for genre_link in response.css("div.zanrovi a"):
            genre_url = genre_link.attrib["href"]
            genre_name = genre_link.css("::text").get()

            yield response.follow(genre_url, callback=self.parse_books, cb_kwargs={"genre": genre_name})

    def parse_books(self, response, genre):
        for book in response.css("div.knjiga"):
            title = book.css("div.podaci a.naslov::text").get()
            authors = book.css("div.podaci a::text").getall()
            authors_list = []
            for a in authors:
                if a and a != title:
                    authors_list.append(a)
            if title is not None:
                yield {
                    "title": title,
                    "author": authors_list,
                    "genre": genre,
                    "image": "https://laguna.rs/" + book.css("div.knjiga_img img::attr(src)").get()
                }
