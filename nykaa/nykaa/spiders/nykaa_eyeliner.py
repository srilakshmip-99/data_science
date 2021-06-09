import scrapy
from scrapy.http import HtmlResponse

class NykaaEyelinerSpider(scrapy.Spider):
    name = 'nykaa_eyeliner'
    page_number=2
    start_urls = ['https://www.nykaa.com/makeup/eyes/eyeliner/c/240?page_no=1']

    def parse(self, response:HtmlResponse):
        all_data = response.css(".desktop-cart")
        for data in all_data:
            image = data.css("div.listing_img::attr(src)").get()
            name = data.css("div.col-xs-12 h2 span::text").get()
            price = data.css("span.mrp-price::text").getall()
            discount=data.css("span.post-card__offers-offer ::text").get()
            discount_price= data.css("span.post-card__content-price-offer::text").getall()

            yield {
                "image":image,
                "name":name,
                "price":price,
                "DiscountPercent":discount,
                "DiscountPrice":discount_price,
            }
        url = 'https://www.nykaa.com/makeup/eyes/eyeliner/c/240?page_no='+str(self.page_number)

        if self.page_number <=15:
            self.page_number+=1
            yield response.follow(url, self.parse)

