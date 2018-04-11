# -*- coding:utf-8 -*-


import json
import scrapy
import logging
from bs4 import BeautifulSoup
from lianjia_spider.settings import table
from lianjia_spider.items import LianjiaSpiderItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    base_url = 'https://bj.lianjia.com/ershoufang/'

    def start_requests(self):
        district = ['dongcheng', 'xicheng', 'chaoyang', 'haidian', 'fengtai', 'shijingshan', 'tongzhou', 'changping',
                    'daxing', 'yizhuangkaifaqu', 'shunyi', 'fangshan', 'mentougou', 'pinggu', 'huairou',
                    'miyun', 'yanqing', 'yanjiao', 'xianghe']
        for elem in district:
            region_url = self.base_url + elem
            yield scrapy.Request(url=region_url, callback=self.page_navigate)

    def page_navigate(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        try:
            pages = soup.find_all("div", class_="house-lst-page-box")[0]
            if pages:
                dict_number = json.loads(pages["page-data"])
                max_number = dict_number['totalPage']
                for num in range(1, max_number + 1):
                    url = response.url + 'pg' + str(num) + '/'
                    yield scrapy.Request(url=url, callback=self.parse)
        except:
            logging.info("*******该地区没有二手房信息********")

    def parse(self, response):
        item = LianjiaSpiderItem()
        soup = BeautifulSoup(response.body, "html.parser")

        #获取到所有子列表的信息
        house_info_list = soup.find_all(name="li", class_="clear")

        # 通过url辨认所在区域
        url = response.url
        url = url.split('/')
        item['Region'] = table[url[-3]]

        for info in house_info_list:
            item['Id'] = info.a['data-housecode']

            house_info = info.find_all(name="div", class_="houseInfo")[0]
            house_info = house_info.get_text()
            house_info = house_info.replace(' ', '')
            house_info = house_info.split('/')
            # print(house_info)
            try:
                item['Garden'] = house_info[0]
                item['Layout'] = house_info[1]
                item['Size'] = house_info[2]
                item['Direction'] = house_info[3]
                item['Renovation'] = house_info[4]
                if len(house_info) > 5:
                    item['Elevator'] = house_info[5]
                else:
                    item['Elevator'] = ''
            except:
                print("数据保存错误")

            position_info = info.find_all(name='div', class_='positionInfo')[0]
            position_info = position_info.get_text()
            position_info = position_info.replace(' ', '')
            position_info = position_info.split('/')
            # print(position_info)
            try:
                item['Floor'] = position_info[0]
                item['Year'] = position_info[1]
                item['District'] = position_info[2]
            except:
                print("数据保存错误")

            price_info = info.find_all("div", class_="totalPrice")[0]
            item['Price'] = price_info.span.get_text()

            yield item

