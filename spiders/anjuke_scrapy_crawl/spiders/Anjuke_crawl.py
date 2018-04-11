# -*- coding:utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from anjuke.items import AnjukeItem

class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    custom_settings = {
        'REDIRECT_ENABLED': False
    }
    start_urls = ['https://beijing.anjuke.com/sale/']

    def start_requests(self):
        base_url = 'https://beijing.anjuke.com/sale/'
        for page in range(1, 51):
            url = base_url + 'p' + str(page) + '/'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        num = len(response.xpath('//*[@id="houselist-mod-new"]/li').extract())
        house_info = response.xpath('//*[@id="houselist-mod-new"]')
        print(house_info)
        for i in range(1, num + 1):
            l = ItemLoader(AnjukeItem(), house_info)

            l.add_xpath('Layout', '//li[{}]/div[2]/div[2]/span[1]/text()'.format(i))
            l.add_xpath('Size', '//li[{}]/div[2]/div[2]/span[2]/text()'.format(i))
            l.add_xpath('Floor', '//li[{}]/div[2]/div[2]/span[3]/text()'.format(i))
            l.add_xpath('Year', '//li[{}]/div[2]/div[2]/span[4]/text()'.format(i))
            l.add_xpath('Garden', '//li[{}]/div[2]/div[3]/span/text()'.format(i))
            l.add_xpath('Region', '//li[{}]/div[2]/div[3]/span/text()'.format(i))
            l.add_xpath('Price', '//li[{}]/div[3]/span[1]/strong/text()'.format(i))

            yield l.load_item()




