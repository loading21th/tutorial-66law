import scrapy 
from  tutorial.items import TutorialItem 
from scrapy.http import Request

class x66lawSpider(scrapy.Spider):
    name="66law"
    base_ual_pri = "http://www.66law.cn/question/list_"
    base_ual_last = "_r1.aspx"
    start_urls = [
            "http://www.66law.cn/question/list_1_r1.aspx"
            ]
    
    def parse(self,response):
        for i in range(1,150):
            base_ual_pri = "http://www.66law.cn/question/list_"
            base_ual_last = "_r1.aspx"
            base_url = base_ual_pri + str(i) + base_ual_last
            yield Request(url=base_url, callback=self.get_more)
    
    def get_more(self,response):
        root_url = "http://www.66law.cn"
        questions = response.xpath('//td[@class="zx_lb_bt"]/a[2]/@href')
        '''
        target_url = root_url + questions[1].extract() 
        return  Request(url=target_url,callback=self.grap_message)
        '''
        for question in questions:
            target_url = root_url + question.extract() 
            yield Request(url=target_url,callback=self.grap_message)
        
    def grap_message(self,response):
        item = TutorialItem()
        useful_items = response.xpath('//div[@class="cont-list"]/div')
        item['question'] = useful_items[0].xpath('./span/text()').extract()
        item['answer']=[]
        for index in range(2,len(useful_items)):
            item['answer'].append(useful_items[index].xpath('./div[@class="answer-box"]/p[1]/text()').extract())
        return item
