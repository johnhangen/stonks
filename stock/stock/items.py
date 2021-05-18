# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like
    name = scrapy.Field()
    price = scrapy.Field()
    change_per = scrapy.Field()
    previous_close = scrapy.Field()
    Open = scrapy.Field()
    Bid = scrapy.Field()
    Ask_per = scrapy.Field()
    day_range = scrapy.Field()
    weeks_range = scrapy.Field()
    volume = scrapy.Field()
    avg_volume = scrapy.Field()
    market_cap = scrapy.Field()
    beta = scrapy.Field()
    pe_ratio = scrapy.Field()
    eps = scrapy.Field()
    earnings_date = scrapy.Field()
    forward_div_yel = scrapy.Field()
    ex_div_date = scrapy.Field()
    target_est = scrapy.Field()

