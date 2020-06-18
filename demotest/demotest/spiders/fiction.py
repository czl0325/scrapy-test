# -*- coding: utf-8 -*-
import scrapy
from demotest.items import FictionItem


class FictionSpider(scrapy.Spider):
    name = 'fiction'
    allowed_domains = ['81zw.com']
    start_urls = ['https://www.81zw.com/book/32145/14735342.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = '\n'.join(response.xpath('//div[@id="content"]/text()').extract())
        yield FictionItem(title=title, content=content)
        catalog = response.xpath('//div[@class="bottem1"]/a[2]/@href').extract_first()
        next_url = response.xpath('//div[@class="bottem1"]/a[3]/@href').extract_first()
        if next_url != catalog:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
