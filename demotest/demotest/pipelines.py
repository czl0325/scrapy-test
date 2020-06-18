# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DemotestPipeline:
    def process_item(self, item, spider):
        return item


class FictionPipeline:
    def open_spider(self, spider):
        self.file = open("北宋大丈夫.txt", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print(item["title"])
        self.file.write(item["title"] + "\n\n" + item["content"] + "\n\n")
        return item
