# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TyworkItem(scrapy.Item):
    job_id = scrapy.Field()
    job_title = scrapy.Field();
    job_salary = scrapy.Field();
    job_desc = scrapy.Field();
    job_type = scrapy.Field();
    job_position = scrapy.Field();
    job_contact = scrapy.Field();
    job_text = scrapy.Field();
    job_href = scrapy.Field();
    job_dq = scrapy.Field();
    job_zz = scrapy.Field();
    job_nr = scrapy.Field();
    job_dx = scrapy.Field();
    job_xs = scrapy.Field();
    job_rs = scrapy.Field();

