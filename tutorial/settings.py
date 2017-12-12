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
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
ITEM_PIPELINES = {'tutorial.pipelines.JsonWithEncodingPipeline':300}
DOWNLOADER_MIDDLEWARES = {  
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    'tutorial.middlewares.ProxyMiddleWare':400,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,  
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None  
} 
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
