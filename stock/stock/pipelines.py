# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter

class StockPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            username = 'root', 
            passwd  = 'Cps.49801439', 
            database = 'stonks'
            )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS stonks_tb""")
        self.curr.execute("""CREATE TABLE stonks_tb(
                            name text,
                            price text,
                            change_per text,
                            previous_close text,
                            Open text,
                            Bid text,
                            Ask_per text,
                            day_range text,
                            weeks_range text,
                            volume text,
                            avg_volume text,
                            market_cap text,
                            beta text,
                            pe_ratio text,
                            eps text,
                            earnings_date text,
                            target_est text
                            )""")

    def process_item(self, item, Spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into stonks_tb values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                    item['name'][0],
                    item['price'][0],
                    item['change_per'][0],
                    item['previous_close'][0],
                    item['Open'][0],
                    item['Bid'][0],
                    item['Ask_per'][0],
                    item['day_range'][0],
                    item['weeks_range'][0],
                    item['volume'][0],
                    item['avg_volume'][0],
                    item['market_cap'][0],
                    item['beta'][0],
                    item['pe_ratio'][0],
                    item['eps'][0],
                    item['earnings_date'][0],
                    item['target_est'][0]
        ))
        self.conn.commit()