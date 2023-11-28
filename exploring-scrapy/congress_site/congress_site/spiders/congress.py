import scrapy

class CongressSpider(scrapy.Spider):
    name = "congress"
    allowed_domains = ["congress.gov"]
    start_urls = ["https://www.congress.gov/img/member/j000288_200.jpg"]

    # Proxy settings
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'congress_site.middlewares.ProxyMiddleware': 543,  # Adjust the priority as needed
        },
    }

    def parse(self, response):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RESPONSE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        pass


