# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['https://maoyan.com/films?showType=2']
    start_urls = ['https://maoyan.com/']

    def parse(self, response):
        names = response.xpath('//dl[@class="movie-list"]/dd//div[contains(@class, "movie-title")]/@title').extract()

        print(names)
