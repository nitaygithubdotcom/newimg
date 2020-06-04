# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlimagesItem

class ImagesSpider(scrapy.Spider):
    name = 'images'
    start_urls = ['https://www.cricbuzz.com/profiles/9311/jasprit-bumrah/']

    def parse(self, response):
        item = CrawlimagesItem()
        img_url = []
        src = response.xpath('//div[@class="cb-col cb-col-20 cb-col-rt"]/img/@src').get()
        img_url.append(response.urljoin(src))
        item["image_urls"] = img_url
        return item
        