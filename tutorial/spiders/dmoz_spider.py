# -*- coding:utf-8 -*- 
import codecs
import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
class DmozSpider(Spider):
  name = "dmoz"
  allowed_domains = ["dianping.com"]
  pagenum=1
  start_urls = [
"http://www.dianping.com/search/category/267/10/g248"
]
#  def start_requests(self):  
 #   yield scrapy.Request("http://www.dianping.com/search/category/1/10/g110p1",
  #                headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOsW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"})  
  def parse(self, response):
	hxs=Selector(response)
	sites=hxs.xpath('//span[@class="addr"]')
	output = open('result.txt', 'a')
	for site in sites:
		addr=site.xpath('text()').extract()
                for data in addr:
                   strTmp =''
                   strTmp+=data.encode('utf-8')
		print strTmp
                output.write('昆明市'+strTmp+'\n')
	output.close()
        if self.pagenum<4:
            self.pagenum=self.pagenum+1
            baseUrl='http://www.dianping.com/search/category/267/10/g248p'+str(self.pagenum)
            print baseUrl
            yield scrapy.Request(baseUrl,callback=self.parse)
