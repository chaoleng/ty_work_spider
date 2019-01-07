# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import scrapy

def dbHandle():
    conn = pymysql.connect(
        user="tywork",
        password="tywork",
        port=3306,
        host="127.0.0.1",   #本地数据库  等同于localhost
        db="ty_tokyo",      #数据库名
        charset="utf8"

    )
    return conn

class TyworkPipeline(object):        
     def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        # print(item['job_desc'])
        job_id = item['job_id']
        job_title = item['job_title']
        job_salary = item['job_salary']        
        job_desc = item['job_desc']
        # job_type = item['job_type']
        job_position = item['job_position']
        print(job_position)
        # sql = "replace into ty_tokyo.job(job_desc) values(%s)"
        sql = "replace into ty_tokyo.job(job_id,job_title,job_salary,job_desc,job_position) values(%s,%s,%s,%s,%s)"
        try:
             # cursor.execute(sql,(item['job_id'],item['job_title'],item['job_salary'],item['job_desc'],item['job_type'],item['job_position']))
             # cursor.execute(sql,(job_desc))
             cursor.execute(sql,(job_id,job_title,job_salary,job_desc,job_position))
             # print(item+'存储中')
             dbObject.commit()
        except Exception as e:
             print (e)
             dbObject.rollback()
        return item
        # print(item+'存储中')