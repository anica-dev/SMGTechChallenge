To run the project:

docker build -t scrapingapp_image .

docker run -d --name scrapingapp -p 8000:8000 scrapingapp_image

Postman collection for testing can be found in postman folder.