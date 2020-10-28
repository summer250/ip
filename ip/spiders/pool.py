# -*- coding: utf-8 -*-
import scrapy
from ip.items import IpItem


class PoolSpider(scrapy.Spider):
    name = 'pool'
    allowed_domains = ['ip.jiangxianli.com']
    start_urls = ['https://ip.jiangxianli.com/?page=1&country=%E4%B8%AD%E5%9B%BD']

    def parse(self, response):
        for page in range(1,8):
            url = 'https://ip.jiangxianli.com/?page='+str(page)+'&country=%E4%B8%AD%E5%9B%BD'
            yield scrapy.Request(url=url,callback=self.parse_ip)

    def parse_ip(self, response):
        tr_list = response.css("div.layui-form>table>tbody>tr")
        for tr in tr_list:
            item = IpItem()

            # ip地址
            ip = tr.css('td:nth-child(1)::text').get()
            item['ip'] = ip

            # 端口号
            port = tr.css('td:nth-child(2)::text').get()
            item['port'] = port

            # 匿名度
            anons = tr.css('td:nth-child(3)::text').get()
            item['anons'] = anons

            # 类型：http/https
            schema = tr.css('td:nth-child(4)::text').get()
            item['schema'] = schema

            # 国家
            position = tr.css('td:nth-child(5)::text').get()
            item['position'] = position

            # 位置
            country = tr.css('td:nth-child(6)::text').get()
            item['country'] = country

            # 响应速度
            speed = tr.css('td:nth-child(8)::text').get()
            item['schema'] = schema

            # 最后验证时间
            verify_time = tr.css('td:nth-child(10)::text').get()
            item['verify_time'] = verify_time









            item['speed'] = speed

            print(item)
            yield item
