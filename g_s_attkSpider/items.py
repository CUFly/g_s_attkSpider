# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GSAttkspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    group = scrapy.Field()
    g_id = scrapy.Field()
    Associated_Groups = scrapy.Field()
    softwares = scrapy.Field()
    # Techniques_Used = scrapy.Field()
