# -*- coding:utf-8 -*- tutorial
import scrapy # 导入scrapy包

from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from tutorial.items import DmozItem, CurrencyItem
import json, MySQLdb, time, os
import datetime

class Eth2Spider(scrapy.Spider):
    handle_httpstatus_list = [403, 503]
    name = 'eth2'
    bash_url = 'https://etherscan.io'

    def start_requests(self):
        url = self.bash_url + "/tokens"
        yield Request(url, self.start_response)

    def start_response(self, response):
        start = response.xpath('//body/div/div[4]/div[2]/div[2]/p/span/b[1]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
        end = response.xpath('//body/div/div[4]/div[2]/div[2]/p/span/b[2]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

        for i in range(int(start), int(end) + 1):
            url = self.bash_url + "/tokens?p=" + str(i)
            request = Request(url, self.parseOne)
            request.meta['end'] = end
            yield request

    def parseOne(self, response):
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

            #url = self.bash_url + "/token/" + token + "#tokenInfo"
            #request = Request(url, callback=self.TokenInfo)
            #request.meta['token'] = token
            #yield request

        self.execute_sql(sql[:-1])

    def TokenInfo(self, response):
        token = str(response.meta['token'])

        table1_arr = response.xpath('//body/div/div[4]/div[1]/div[1]/table/tr')
        table2_arr = response.xpath('//body/div/div[4]/div[1]/div[2]/table/tr')
        TotalSupply     = ""
        Value_Per_Token = ""
        Token_Holders   = ""
        NO_Of_Transfers = ""

        ERC20_Contract  = ""
        decimals        = ""

        if len(table1_arr)>0:
            if table1_arr[0].xpath('td[2]'):
                TotalSupply = table1_arr[0].xpath('td[2]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            if table1_arr[1].xpath('td[2]'):
                Value_Per_Token = table1_arr[1].xpath('td[2]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            if table1_arr[2].xpath('td[2]'):
                Token_Holders = table1_arr[2].xpath('td[2]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            if table1_arr[3].xpath('td[2]'):
                NO_Of_Transfers = table1_arr[3].xpath('td[2]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

        if len(table2_arr)>0:
            if table1_arr[0].xpath('td[0]'):
                ERC20_Contract = table1_arr[0].xpath('td[0]/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            if table1_arr[1].xpath('td[1]'):
                decimals = table1_arr[1].xpath('td[1]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

        print "================== |||||||||||||||||||||||||||| ================================="
        print ":token:" + token
        print ":TotalSupply:" + TotalSupply
        print ":Value_Per_Token:" + Value_Per_Token
        print ":Token_Holders:" + Token_Holders
        print ":NO_Of_Transfers:" + NO_Of_Transfers

        print ":ERC20_Contract:" + ERC20_Contract
        print ":decimals:" + decimals

        print "================== |||||||||||||||||||||||||||| ================================="
        # TODO 数据了插入

    def Transfers(self, response):
        token = str(response.meta['token'])
        # fo = open("foo.txt", "w")
        # fo.write(response.body)
        kt = 0
        sql = """INSERT INTO token_transfers(`Token`, `Tx_Hash`, `Age`, `From`, `type`, `To`, `Quantity`, `create_at`) VALUES """
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

            sql += "('" + token + "', '" + TxHash + "', '" + str(date_time) + "', '" + From + "', '" + type_img + "', '" + To + "', '" + Quantity + "', '" + _time + "'),"

        self.execute_sql(sql[:-1])

    def Holders(self, response):
        token = str(response.meta['token'])
        # fo = open("foo.txt", "w")
        # fo.write(response.body)
        kt = 0
        sql = """INSERT INTO token_holders(`Token`, `Rank`, `Address`, `Quantity`, `Percentage`, `create_at`) VALUES """
        for sel in response.xpath('//table/tr'):
            # Index
            if kt == 0:
                kt = 1
                continue

            # Rank
            Rank = sel.xpath('td[1]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Address
            Address = sel.xpath('td[2]/span/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Quantity
            Quantity = sel.xpath('td[3]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            # Percentage
            Percentage = sel.xpath('td[4]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

            _time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print Rank
            print Address
            print Quantity
            print Percentage
            print " ======================================================= "
            sql += "('" + token + "', '" + Rank + "', '" + Address + "', '" + Quantity + "', '" + Percentage + "', '" + _time + "'),"

        #print sql[:-1]
        self.execute_sql(sql[:-1])

    def HoldersTransfers(self, response):
        print "==============================="
        fo = open("foo.txt", "w")
        fo.write(response.body)

        kt = 0
        for sel in response.xpath('//table/tr'):
            # Index
            if kt == 0:
                kt = 1
                continue

            # Rank
            Rank = sel.xpath('td[1]/span/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')
            print Rank
        print "==============================="

    @staticmethod
    def objToStr(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def execute_sql(sql):
        db = MySQLdb.connect("localhost", "root", "123456", "etherscan_db")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

    # 把字符串转成datetime
    @staticmethod
    def string_toDatetime(string):
        return datetime.datetime.strptime(string, "%b-%d-%Y %I:%M:%S %p").strftime("%Y-%m-%d %H:%S:%M")
