# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

def list2str(value):
    new = ''.join(value).strip()
    return new

class AnjukePipeline(object):
    def process_item(self, item, spider):
        size = item['Size']
        price = item['Price']
        region = item['Region']
        garden = item['Garden']
        layout = item['Layout']
        year = item['Year']
        floor = item['Floor']

        item['Size'] = int(re.findall(r'\d+', list2str(size))[0])
        item['Year'] = int(re.findall(r'\d+', list2str(year))[0])
        item['Floor'] = int(re.findall(r'\d+', list2str(floor))[0])
        item['Price'] = list2str(price)
        item['Layout'] = list2str(layout)

        garden = re.findall(r'(.*?)\xa0\xa0', list2str(garden))[0]
        region = re.findall(r'.*?(.+?-.+?-.+?)', list2str(region))[0]
        item['Region'] = region.replace('\t', '').replace('\n', '').strip()
        item['Garden'] = garden.replace('\t', '').replace('\n', '')
        return item
