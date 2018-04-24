# -*- coding:utf-8 -*- tutorial
import scrapy # 导入scrapy包

from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from tutorial.items import DmozItem, CurrencyItem
import json, MySQLdb, time, os
import datetime

class EthSpider(scrapy.Spider):
    handle_httpstatus_list = [403, 503]
    name = 'eth'
    bash_url = 'https://etherscan.io'

    def start_requests(self):
        #self.execute_sql("truncate table `tokens`;")
        #url = self.bash_url + "/tokens?p=1"
        #yield Request(url, self.parseOne)
        request = Request("https://etherscan.io/token/generic-tokentxns2?contractAddress=0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0&a=&mode=", callback=self.Transfers)
        request.meta['token'] = '0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0'
        request.meta['p'] = '1'
        yield request

        #for i in range(1, 10):
        #    print i
        #    url = self.bash_url + "/tokens?p=" + str(i)
        #    yield Request(url, self.parseOne)

    def parseOne(self, response):
        items = []

        sql = """INSERT INTO tokens(c_index, name_str, name_simple, icons, token, describes, price, changes, volume_24, market_cap, create_at) VALUES """
        for sel in response.xpath('//tbody/tr'):
            # Index
            index = sel.xpath('td[1]/b/span/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Token
            token_str = sel.xpath('td[2]/a/@href').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            tokenarr = token_str.split("/")
            token = tokenarr[-1]

            # Img
            icons = sel.xpath('td[2]/a/img/@src').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Name And Describes
            name_strs = sel.xpath('td[3]/h5/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            name_list = name_strs.split('(')
            name_str  = name_list[0]
            name_str2 = name_list[-1].split(')')
            name_simple = name_str2[0]

            # Describes
            describes = ""
            if len(sel.xpath('td[3]/small/font/text()').extract()) > 0:
                describes = sel.xpath('td[3]/small/font/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Price
            price = sel.xpath('td[5]/span/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # %Change
            change = ""
            if sel.xpath('td[6]/font'):
                change = sel.xpath('td[6]/font/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            else:
                change = sel.xpath('td[6]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Volume (24h)
            volume_24h = sel.xpath('td[7]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # MarketCap
            market_cap = sel.xpath('td[8]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            _time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #print "================ Start ==========================="
            #print index
            #print index + " : Token : " + token
            #print index + " : Img : " + icons
            #print index + ' : Name Simple : ' + name_simple
            #print index + ' : Name_Str : ' + name_str
            #print index + " : describes : " + describes
            #print index + " : Price : " + price
            #print index + " : Change 1 : " + change
            #print index + " : Volume : " + volume_24h
            #print index + " : MarketCap : " + market_cap
            #print index + " : time : " + _time
            #print "================  End  ==========================="

            # c_index, name_str, name_simple, icons, token, describes, price, change, volume_24, market_cap, create_at
            sql += "(" + index + ", '" + name_str + "', '" + name_simple + "', '" + icons + "', '" + token + "', '" + describes.replace("""'""", """\\'""") + "', '" + price + "', '" + change + "', '" + volume_24h + "', '" + market_cap + "', '" + _time + "'),"

            #for i in range(1, 10):
            #    url = self.bash_url + "/token/generic-tokentxns2?contractAddress=" + token + "&p=" + str(i)
            #    request = Request(url, callback=self.transfers)
            #    request.meta['token'] = token
            #    request.meta['p'] = str(i)
            #    yield request

        for i in range(1, 10):
                url = self.bash_url + "/token/generic-tokentxns2?contractAddress=0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0&a=&mode=&p=" + str(i)
                request = Request(url, callback=self.Transfers)
                request.meta['token'] = token
                request.meta['p'] = str(i)
                yield request
        #print sql[:-1]
        self.execute_sql(sql[:-1])

    def Transfers(self, response):
        token = str(response.meta['token'])
        # fo = open("foo.txt", "w")
        # fo.write(response.body)
        kt = 0
        sql = """INSERT INTO token_transfers(Token, Tx_Hash, Age, From, type, To, Quantity, create_at) VALUES """
        for sel in response.xpath('//table/tr'):
            # Index
            if kt == 0:
                kt = 1
                continue

            # TxHash
            TxHash = sel.xpath('td[1]/span/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Age
            Age     = sel.xpath('td[2]/span/@title').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            Age_Str = sel.xpath('td[2]/span/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            date_time = self.string_toDatetime(Age)

            # From
            From = sel.xpath('td[3]/span/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # type_img
            type_img = sel.xpath('td[4]/img/@src').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # To
            To = sel.xpath('td[5]/span/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Quantity
            Quantity = sel.xpath('td[6]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            _time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            #print " : TxHash : " + TxHash
            #print " : Age : " + date_time
            #print " : Age_Str : " + Age_Str
            #print " : From : " + From
            #print " : type_img : " + type_img
            #print " : To : " + To
            #print " : Quantity : " + Quantity
            #print " ========================================================= "

            # Token, Tx_Hash, Age, From, type, To, Quantity, create_at
            sql += "(" + token + ", '" + TxHash + "', '" + date_time + "', '" + From + "', '" + type + "', '" + To + "', '" + Quantity + "', '" + _time + "'),"

        print sql[:-1]
        self.execute_sql(sql[:-1])

    @staticmethod
    def objToStr(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def execute_sql(sql):
        db = MySQLdb.connect("localhost", "root", "123456", "etherscan_db")
        cursor = db.cursor()
        try:
            # print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            cursor.execute(sql)
            db.commit()
        except:
            # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
            db.rollback()

        db.close()

    # 把字符串转成datetime
    @staticmethod
    def string_toDatetime(string):
        return datetime.datetime.strptime(string, "%b-%d-%Y %I:%M:%S %p")
