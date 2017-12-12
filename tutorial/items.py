# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    detail = scrapy.Field()
    answer1 = scrapy.Field()
    answer2 = scrapy.Field()
    answer3 = scrapy.Field()
    answer4 = scrapy.Field()
    answer5 = scrapy.Field()

