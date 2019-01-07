# -*- coding: utf-8 -*-
import scrapy
from tywork.items import TyworkItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spidermiddlewares.httperror import HttpError

class TyworkSpiderSpider(scrapy.Spider):
    name = 'tywork_spider'
    allowed_domains = ['8n8n.co.jp']
    start_urls = ['http://8n8n.co.jp/job/']

    def parse(self, response):
        job_list = response.xpath("//div[@class='wot-oneII']")
        for i_item in job_list:
            item = TyworkItem()               
            # items=[]
            item['job_id'] = i_item.xpath("//a//text()").extract_first()
            item['job_salary'] = i_item.xpath("//div[@class='wot-two-onet']//div[@class='wot-two-three']//ul//li//span[@id='z1kpt6']//text()").extract_first()
            item['job_salary']  = "".join(item['job_salary'].split())
            item['job_title'] = i_item.xpath("//div[@class='six-a']//a//text()").extract_first()
            #item['job_desc'] = i_item.xpath("//div[@class='wot-two-onet']//span[@id='z1kpt8']//text()").extract_first()
            #item['job_desc'] = "".join(item['job_desc'].split())
            item['job_type'] = i_item.xpath("//div[@class='wot-two-four000']//li//input//@value").extract_first()
            item['job_position'] = i_item.xpath('normalize-space(//li//div)').extract_first()
            item['job_position'] = "".join(item['job_position'].split())
            # yield item
            # items.append(item)
            
            # work_item['job_text'] = i_item.xpath("//div[@class='wot-two11']//b//a/@href").extract_first()
            # work_item['job_contact'] = i_item.xpath("//div[@class='wot-two11']//b//a/@href").extract_first()
            #将数据yield到pipeline里面，进行数据的清洗和存储
            # yield work_item

            # 深度解析页面数据
            # work_item['job_href'] = i_item.xpath("//div[@class='wot-two11']//b//a/@href").extract_first()
            item['job_href'] = i_item.xpath("//div[@class='wot-two11']//b//a/@href").extract_first()
            item['job_id'] = item['job_href'][27:].strip('/')  #获取job_id为了方式数据重复
            # item['job_desc'] = response.meta['job_desc']
            
            # print(item['job_id'])
            # yield scrapy.Request(url=item['job_href'],meta={'item_1': item},callback=self.parse_job)

            yield scrapy.Request(url=item['job_href'], meta={'item_1': item},
                                 callback=self.parse_job, dont_filter=True)    
            # yield work_item


         #解析下一页
        next_link = response.xpath("//div[@class='ul-ll-one']//li//a[text()='下一页']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request(next_link,callback=self.parse)

    def parse_job(self,response):
        item = TyworkItem()
        item_1 = response.meta['item_1']
        html = HtmlXPathSelector(response)
        #print 'response ',response
        page = html.xpath("//div[@id='khu8iop1']")
        # item['job_id'] = item_1['job_id']
        # item['job_title'] = item_1['job_title']
        # item['job_salary'] = item_1['job_salary']
        # item['job_position'] = item_1['job_position']
        # print (page)
        #print 'page ',page
        # items = []
        for i in page:
            item['job_id'] = item_1['job_id']
            item['job_title'] = item_1['job_title']
            item['job_salary'] = item_1['job_salary']
            item['job_position'] = item_1['job_position']
        # item['job_href'] = item_1['job_href'].encode('utf8')
            # item['job_dq'] = i.xpath("//div[@id='home2C-0']//table//td//font//text()").extract_first()
            # item['job_dq'] = "".join(item['job_dq'].split())
            item['job_desc'] = response.xpath('normalize-space(//div[@id="khu8iop"]//div[@id="khu8iop1"]//div[@id="home2-1-0-0-0-M2S"]//div[@id="home2C-0"]//table//tr)').extract_first()
            #print i.xpath('text()').extract(),i.xpath('@href').extract()
            # print ("".join(item['job_position'].split()))
            # items.append(item)
            yield item
            # return items



