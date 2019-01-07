# -*- coding:utf-8 -*-
import pymysql
conn = pymysql.connect(
  user="tywork",
  password="tywork",
  port=3306,
  host="127.0.0.1",   #本地数据库  等同于localhost
  db="ty_tokyo",      #数据库名
  charset="utf8"
)
cur = conn.cursor()      #获取对应的操作游标
query = 'select count(*) from job'
cur.execute(query)
data = cur.fetchone()
print(data)
cur.close()
conn.commit()
conn.close()
