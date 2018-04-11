# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class LianjiaSpiderPipeline(object):
    def process_item(self, item, spider):
        size = item['Size']
        year = item['Year']
        floor = item['Floor']

        item['Size'] = float(re.findall(r'\d*', size)[0])
        item['Year'] = int(re.findall(r'\d*', year)[0])
        item['Floor'] = re.findall(r'.*?\(.(\d*).\).*?', floor)[0]
        return item
