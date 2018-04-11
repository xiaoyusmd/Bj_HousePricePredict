# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl anjuke -o anjuke.csv".split())