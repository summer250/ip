# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import redis


class IpPipeline:
    def open_spider(self, spider):
        host = spider.settings.get("REDIS_HOST")
        port = spider.settings.get("REDIS_PORT")

        self.db_conn = redis.StrictRedis(host=host, port=port)

    def process_item(self, item, spider):
        item_dict = dict(item)
        self.db_conn.rpush("iplist", '{}://{}:{}'.format(item['schema'].lower(), item['ip'], item['port']))
        return item

    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()
