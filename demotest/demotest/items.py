# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemotestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FictionItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
