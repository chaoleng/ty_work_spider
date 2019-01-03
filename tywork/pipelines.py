# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='douban',
        passwd='douban',
        charset='utf8',
        use_unicode=False
    )
    return conn

class TyworkPipeline(object):
        
     def process_item(self, item, spider):
        # dbObject = dbHandle()
        # cursor = dbObject.cursor()
        # job_id = item['job_id'].join
        # job_title = scrapy.Field();
        # job_salary = scrapy.Field();
        # job_desc = scrapy.Field();
        # job_type = scrapy.Field();
        # job_position = scrapy.Field();
        # sql = "replace into tywork.tywork(serial_number,movie_name,introduce,star,evaluate,describ) values(%s,%s,%s,%s,%s,%s)"
        # try:
        #      cursor.execute(sql,(item['serial_number'],item['movie_name'],item['introduce'],item['star'],item['evaluate'],item['describ']))
        #      dbObject.commit()
        # except Exception as e:
        #      print (e)
        #      dbObject.rollback()
        return item
