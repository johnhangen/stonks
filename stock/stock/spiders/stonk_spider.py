import scrapy
from ..items import StockItem

class stockSpider(scrapy.Spider):
    name = "stonk"
    allowed_domains = ['yahoo.com']

    stock = str(input('Enter stonk ticker: '))

    start_urls = [
        f'https://finance.yahoo.com/quote/{stock}',
    ]

    def parse(self, response):

        items = StockItem()

        #  Bases
        top_base = response.xpath('//div[contains(@data-test,"quote-header")]')
        left_base = response.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody')
        right_base = response.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody')

        #  Top
        name = top_base.xpath('div[2]/div[1]/div[1]/h1/text()').extract()
        price = top_base.xpath('div[3]/div[1]/div[1]/span[1]/text()').extract()
        change_per = top_base.xpath('div[3]/div[1]/div[1]/span[2]/text()').extract()

        #  Left
        previous_close = left_base.xpath('tr[1]/td[2]/span/text()').extract()
        Open = left_base.xpath('tr[2]/td[2]/span/text()').extract()
        Bid = left_base.xpath('tr[3]/td[2]/span/text()').extract()
        Ask_per = left_base.xpath('tr[4]/td[2]/span/text()').extract()
        day_range = left_base.xpath('tr[5]/td[2]/text()').extract()
        weeks_range = left_base.xpath('tr[6]/td[2]/text()').extract()
        volume = left_base.xpath('tr[7]/td[2]/span/text()').extract()
        avg_volume = left_base.xpath('tr[8]/td[2]/span/text()').extract()
        
        #  Right
        market_cap = right_base.xpath('tr[1]/td[2]/span/text()').extract()
        beta = right_base.xpath('tr[2]/td[2]/span/text()').extract()
        pe_ratio = right_base.xpath('tr[3]/td[2]/span/text()').extract()
        eps = right_base.xpath('tr[4]/td[2]/span/text()').extract()
        earnings_date = right_base.xpath('tr[5]/td[2]/span/text()').extract()
        forward_div_yel = right_base.xpath('tr[6]/td[2]/text()').extract()
        ex_div_date = right_base.xpath('tr[7]/td[2]/span/text()').extract()
        target_est = right_base.xpath('tr[8]/td[2]/span/text()').extract()

        items['name'] = name
        items['price'] = price
        items['change_per'] = change_per
        items['previous_close'] = previous_close
        items['Open'] = Open
        items['Bid'] = Bid
        items['Ask_per'] = Ask_per
        items['day_range'] = day_range
        items['weeks_range'] = weeks_range
        items['volume'] = volume
        items['avg_volume'] = avg_volume
        items['market_cap'] = market_cap
        items['beta'] = beta
        items['pe_ratio'] = pe_ratio
        items['eps'] = eps
        items['earnings_date'] = earnings_date
        items['forward_div_yel'] = forward_div_yel
        items['ex_div_date'] = ex_div_date
        items['target_est'] = target_est

        yield items