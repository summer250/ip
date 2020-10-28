# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IpItem(scrapy.Item):
    # define the fields for your item here like:

    # ip地址
    ip = scrapy.Field()
    # 端口号
    port = scrapy.Field()
    # 匿名度
    anons = scrapy.Field()
    # 类型：http/https
    schema = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 位置
    position = scrapy.Field()
    # 响应速度
    speed = scrapy.Field()
    # 最后验证时间
    verify_time = scrapy.Field()
