from scrapy import cmdline #爬虫启动
print("Spider start-----------------")
cmdline.execute('scrapy crawl tywork_spider'.split())
