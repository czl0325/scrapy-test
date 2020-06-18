# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from demotest.items import FictionItem

class Fiction2Spider(scrapy.Spider):
    name = 'fiction2'
    allowed_domains = ['81zw.com']
    start_urls = ['https://www.81zw.com/book/42724/']

    rules = [
        Rule(LinkExtractor(restrict_xpaths=r'//dl/dd[1]/a'),callback="parse_item"),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[3]'),callback="parse_item")
    ]

    def parse_item(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = '\n'.join(response.xpath('//div[@id="content"]/text()').extract())
        yield FictionItem(title=title, content=content)
