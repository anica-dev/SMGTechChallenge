To run the project:

docker build -t bookscraper_image . 

docker run --rm -v $(pwd)/output:/app bookscraper_image 


Csv file with scraped books is generated in output folder.