# *-* coding:utf-8 *-*  
'''
import random  
import scrapy  
from scrapy import log  
  
  
# logger = logging.getLogger()  
  
class ProxyMiddleWare(object):  
    """docstring for ProxyMiddleWare"""  
    def process_request(self,request, spider):  
        """对request对象加上proxy"""
        proxy = self.get_random_proxy()  
        print("this is request ip:"+proxy)  
        request.meta['proxy'] = proxy   
  
    def process_response(self, request, response, spider):  
        """对返回的response处理"""  
        # 如果返回的response状态不是200，重新生成当前request对象  
        if response.status != 200:  
            proxy = self.get_random_proxy()  
            print("this is response ip:"+proxy)  
            # 对当前reque加上代理  
            request.meta['proxy'] = proxy   
            return request  
        return response  
  
    def get_random_proxy(self):  
        """随机从文件中读取proxy"""  
        while 1:  
            with open('/home/loading_21th/tutorial/proxies.txt', 'r') as f:  
                proxies = f.readlines()  
            if proxies:  
                break  
            else:  
                time.sleep(1)  
        proxy = random.choice(proxies).strip()  
        return proxy
'''
import random
import base64
from settings import PROXIES
class RandomUserAgent(object):
	"""Randomly rotate user agents based on a list of predefined ones"""
	def __init__(self, agents):
		self.agents = agents
	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.getlist('USER_AGENTS'))
	def process_request(self, request, spider):
		#print "**************************" + random.choice(self.agents)
		request.headers.setdefault('User-Agent', random.choice(self.agents))
class ProxyMiddleware(object):
	def process_request(self, request, spider):
		proxy = random.choice(PROXIES)
		if proxy['user_pass'] is not None:
			request.meta['proxy'] = "http://%s" % proxy['ip_port']
			encoded_user_pass = base64.encodestring(proxy['user_pass'])
			request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
			print "**************ProxyMiddleware have pass************" + proxy['ip_port']
		else:
			print "**************ProxyMiddleware no pass************" + proxy['ip_port']
			request.meta['proxy'] = "http://%s" % proxy['ip_port']

	
