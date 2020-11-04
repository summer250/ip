# -*- coding: utf-8 -*-
import scrapy
from ip.items import IpItem
import requests
requests.packages.urllib3.disable_warnings()

class PoolSpider(scrapy.Spider):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    name = 'pool'
    allowed_domains = ['ip.jiangxianli.com']
    test_url = 'https://www.baidu.com/'
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

            # 端口号
            port = tr.css('td:nth-child(2)::text').get()

            # 匿名度
            anons = tr.css('td:nth-child(3)::text').get()

            # 类型：http/https
            schema = tr.css('td:nth-child(4)::text').get()

            # 国家
            position = tr.css('td:nth-child(5)::text').get()

            # 位置
            country = tr.css('td:nth-child(6)::text').get()

            # 响应速度
            speed = tr.css('td:nth-child(8)::text').get()

            # 最后验证时间
            verify_time = tr.css('td:nth-child(10)::text').get()

            # 测试ip可用性
            proxies = {'http': 'https://' + ip+':'+port}
            response1 = requests.get(url=self.test_url, headers=self.headers, proxies=proxies)
            if response1.status_code == 200:
                item['ip'] = ip
                item['port'] = port
                item['anons'] = anons
                item['schema'] = schema
                item['position'] = position
                item['country'] = country
                item['speed'] = speed
                item['verify_time'] = verify_time

                print(item)
                yield item
