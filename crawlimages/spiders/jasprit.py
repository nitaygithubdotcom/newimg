# -*- coding: utf-8 -*-
import scrapy

class PlayerSpider(scrapy.Spider):
    name = 'jasprit'
    start_urls = ['https://www.cricbuzz.com/profiles/9311/jasprit-bumrah/']

    def parse(self, response):
        src = response.xpath('//div[@class="cb-col cb-col-20 cb-col-rt"]/img/@src').get()
        img_url = response.urljoin(src)    
        item["image_urls"] = img_url
        return item
