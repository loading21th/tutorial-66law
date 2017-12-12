# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
ITEM_PIPELINES = {'tutorial.pipelines.JsonWithEncodingPipeline':300}
#DOWNLOADER_MIDDLEWARES = {  
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
#    'tutorial.middlewares.ProxyMiddleWare':400,
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,  
#    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None  
#} 
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#USER_AGENTS = [
#	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#]
PROXIES = [
	{'ip_port': '175.155.77.169:808', 'user_pass': ''},
	{'ip_port': '122.237.106.119:80', 'user_pass': ''},
	{'ip_port': '171.81.89.105:808', 'user_pass': ''},
	{'ip_port': '1114.250.94.95:8118', 'user_pass': ''},
	{'ip_port': '183.133.75.238:8118', 'user_pass': ''},
	{'ip_port': '219.138.58.150:3128', 'user_pass': ''},
	{'ip_port': '114.97.184.92:808', 'user_pass': ''},
	{'ip_port': '42.157.5.154:9999', 'user_pass': ''},
	{'ip_port': '113.92.3.223:9797', 'user_pass': ''},
	{'ip_port': '106.2.6.23:3128', 'user_pass': ''},
	{'ip_port': '112.117.60.29:9999', 'user_pass': ''},
	{'ip_port': '112.80.226.78:8118', 'user_pass': ''},
	{'ip_port': '106.113.242.234:9999', 'user_pass': ''},
	{'ip_port': '113.65.189.121:9797', 'user_pass': ''},
	{'ip_port': '118.113.147.32:8888', 'user_pass': ''},
	{'ip_port': '121.13.165.8:9797', 'user_pass': ''},
	{'ip_port': '106.113.243.205:9999', 'user_pass': ''},
	{'ip_port': '222.222.169.60:53281', 'user_pass': ''},
	{'ip_port': '125.93.149.113:9000', 'user_pass': ''},
	{'ip_port': '180.173.144.50:9797', 'user_pass': ''},
]
COOKIES_ENABLED=False
DOWNLOAD_DELAY=3
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
