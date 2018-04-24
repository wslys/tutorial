# -*- coding:utf-8 -*- tutorial
import scrapy #导入scrapy包

from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from tutorial.items import DmozItem, CurrencyItem
import json, MySQLdb, time, os 

class DmozSpider(scrapy.Spider):
    name = 'eth'
    bash_url = 'https://etherscan.io'

    def start_requests(self):
        for i in range(1, 10):
            url = self.bash_url + "/tokens?p=" + str(i)
            yield Request(url, self.parseOne)

    def parseOne(self, response):
        items = []

        for sel in response.xpath('//tbody/tr'):
            print sel.xpath('td[1]/b/span/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            print sel.xpath('td[2]/a//text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

    def coin(self, response):
        _item = response.meta['item']
        _max_supply = response.xpath('//body/div[4]/div[1]/div[1]/div[4]/div[1]/div[5]/div[2]/span/@data-format-value').extract()
        
        # TODO 
        # print DmozSpider.objToStr(_item)
        max_supply = ""
        if len(_max_supply):
            max_supply = _max_supply[0].strip().encode('unicode-escape').decode('string_escape')
        

        _item['max_supply'] = max_supply
        sql = """INSERT INTO currencys(c_index, name, market_cap, price, volume_24h, circulating_supply, change_24h, max_supply, url, create_at) VALUES """     
        sql += "(" + _item['index'] + ", '" + _item['name'] + "', '" + _item['market_cap'] + "', '" + _item['price'] + "', " + _item['volume_24h'] + ", '" + _item['circulating_supply'] + "', '" + _item['change_24h'] + "', '" + _item['change_24h'] + "', '" + _item['url'] + "', '" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "')"
        
        self.execute_sql(sql)

    def singleMarkets(self, response):
        type_name = str(response.meta['type_name'])
        _index = str(response.meta['index'])

        sql = """INSERT INTO markets(c_index, currency_name, source, pair, volume, price, volumes, create_at) VALUES """
        i = 1
        for sel in response.xpath('//tbody/tr'):
            Index      = sel.xpath('td[1]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Source     = sel.xpath('td[2]/@data-sort').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Pair       = sel.xpath('td[3]/@data-sort').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Volume_24H = sel.xpath('td[4]/@data-sort').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Price      = sel.xpath('td[5]/@data-sort').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Volume_S   = sel.xpath('td[6]/@data-sort').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            if i>100:break
            sql += "('" + _index + "', '" + type_name + "', '" + Source + "', '" + Pair + "', '" + Volume_24H + "', " + Price + ", '" + Volume_S + "', '" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "'),"
            i += 1  

        self.execute_sql(sql[:-1])

    def historicalData(self, response):
        type_name = str(response.meta['type_name'])
        _index = str(response.meta['index'])
        
        sql = """INSERT INTO historical_data(c_index, currency_name, old_date, open, hight, low, close, volume, market_cap, create_at) VALUES """
        for sel in response.xpath('//tbody/tr'):
            Old_date  = sel.xpath('td[1]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Open      = sel.xpath('td[2]/@data-format-value').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            High      = sel.xpath('td[3]/@data-format-value').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Low       = sel.xpath('td[4]/@data-format-value').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Close     = sel.xpath('td[5]/@data-format-value').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Volume    = sel.xpath('td[6]/@data-format-value').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            MarketCap = sel.xpath('td[7]/@data-format-value').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            
            timeStamp = int(time.mktime(time.strptime(Old_date, "%b %d, %Y")))
            localTime = time.localtime(timeStamp) 
            strTime   = time.strftime("%Y-%m-%d %H:%M:%S", localTime) 
            
            sql += "('" + _index + "', '" + type_name + "', '" + strTime + "', '" + Open + "', '" + High + "', " + Low + ", '" + Close + "', '" + Volume + "', '" + MarketCap + "', '" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "'),"
            
        self.execute_sql(sql[:-1])

    @staticmethod
    def objToStr(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def execute_sql(sql):
        db = MySQLdb.connect("localhost", "root", "123456", "tutorial")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()
