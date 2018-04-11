# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
import pymysql
import random
import logging
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

class ProxyMiddleware(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='yuyaodong2587',
                                  charset='utf8')
        self.conn = self.db.cursor()
        self.ip_list = []

    def ip_get(self):
        self.conn.execute('use ip_pool')
        self.conn.execute('select distinct ip, port from iptable')
        data = self.conn.fetchall()

        for elem in data:
            proxy_ip = 'http://' + elem[0] + ':' + elem[1]
            self.ip_list.append(proxy_ip)
        return self.ip_list

    def process_request(self, request, spider):
        random_ip = self.ip_get()
        proxy_ip = random.choice(random_ip)
        if proxy_ip:
            logging.info('******目前正在使用的ip地址是：' + proxy_ip + ' ******')
            request.meta['proxy'] = proxy_ip

    def process_response(self, request, response, spider):
        if response.status != 200:
            proxy_ip = random.choice(self.ip_get())
            request.meta['proxy'] = proxy_ip
        return request
