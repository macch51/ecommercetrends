import scrapy
from scrapy.crawler import CrawlerProcess
import re 

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.com/Best-Sellers/zgbs",
    ]

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def get_substring(self, text, start, end):
        # If pattern pd_rd_i doesn't exist, try extracting via '/dp/<ASIN>'
        pattern = f"{re.escape(start)}(.*?){re.escape(end)}" if start and end else '/dp/([A-Z0-9]{10})'
        match = re.search(pattern, text)
        return match.group(1) if match else None

    def simplify_url(self, url):
            if url.startswith('/'):
                url = f"https://www.amazon.com{url}"
            return url.split('/ref=')[0]

    def parse(self, response):
        for category in response.css("div.a-begin"):
            category_name = category.xpath("div/div/h2/text()").get()
            items = []
            for item in category.css("li.a-carousel-card"):
                title = item.css("div.p13n-sc-truncate-desktop-type2::text").get().strip()
                url = item.css("a.a-link-normal::attr(href)").get()
                asin = self.get_substring(url, 'pd_rd_i=', '&') or self.get_substring(url, None, None)  # Fallback if pd_rd_i pattern fails
                simplified_url = self.simplify_url(url)
                items.append({
                    "title": title,
                    "url": simplified_url,
                    "asin": asin
                })
            
            yield {
                "category": category_name,
                "items": items
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
# Parsing logic here

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "bestsellers.json": {
                "format": "json",
                "indent":2
            },
        },
    })

    process.crawl(AmazonSpider)
    process.start()