# -*- coding:utf-8 -*- tutorial
import scrapy # 导入scrapy包

from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from tutorial.items import DmozItem, CurrencyItem
import json, MySQLdb, time, os
import datetime

class Eth5Spider(scrapy.Spider):
    handle_httpstatus_list = [403, 503]
    name = 'eth5'

    def start_requests(self):
        url = "https://etherscan.io/token/generic-tokenholders2?a=0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0&s=1000000000000000000000000000"
        request = Request(url, self.BasicTokenHolders)
        request.meta['token'] = '0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0'
        yield request

    # 基本的持有者信息
    def BasicTokenHolders(self, response):
        token = str(response.meta['token'])
        end = response.xpath('//body/div[2]/span[2]/b[2]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

        for i in range(1, int(end) + 1):
            time.sleep(1)
            url = "https://etherscan.io/token/generic-tokenholders2?a=" + token + "&s=1E%2b27&p=" + str(i)
            request = Request(url, self.TokenHolders)
            request.meta['token'] = token
            yield request

    #　取所有持有者
    def TokenHolders(self, response):
        token = str(response.meta['token'])
        kt = 0
        sql = """replace into token_holders(`Token`, `Rank`, `Address`, `Quantity`, `Percentage`, `create_at`) VALUES """
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

            sql += "('" + token + "', '" + Rank + "', '" + Address + "', '" + Quantity + "', '" + Percentage + "', '" + _time + "'),"

            # Address 取持有者的交易数据
            url = "https://etherscan.io/token/generic-tokentxns2?contractAddress=" + token + "&a=" + Address + "&mode="
            request = Request(url, self.TokenTransfers)
            request.meta['token'] = token
            request.meta['Address'] = Address
            time.sleep(1)
            yield request

        self.execute_sql(sql[:-1])

    # 持有者的交易数据
    def TokenTransfers(self, response):
        token = str(response.meta['token'])
        Address = str(response.meta['Address'])

        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

        print "========================================================"
        print "=================== token : " + token + " =============="
        print "=================== Address : " + Address + " =========="
        print "========================================================"

        print len(response.xpath('//table/tr'))

        kt = 0
        sql = """INSERT INTO token_transfers(`Token`, `Tx_Hash`, `Age`, `From`, `type`, `To`, `Quantity`, `create_at`) VALUES """

        if len(response.xpath('//table/tr')):
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
                type = sel.xpath('td[4]/span/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

                # To
                To = ""
                if sel.xpath('td[5]/span/a'):
                    To = sel.xpath('td[5]/span/a/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

                # Quantity
                Quantity = sel.xpath('td[6]/text()').extract()[0].strip().encode('unicode-escape').decode('string_escape')

                _time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print " : TxHash : " + TxHash
                print " : Age : " + date_time
                print " : Age_Str : " + Age_Str
                print " : From : " + From
                print " : type_img : " + type
                print " : To : " + To
                print " : Quantity : " + Quantity
                print " ========================================================= "

                sql += "('" + token + "', '" + TxHash + "', '" + str(date_time) + "', '" + From + "', '" + type + "', '" + To + "', '" + Quantity + "', '" + _time + "'),"

            #print sql
            self.execute_sql(sql[:-1])
        else:
            fo = open((str(Address) + ".html"), "w")
            fo.write(response.body)

        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> End >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"



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

    @staticmethod
    def query_sql(sql):
        db = MySQLdb.connect("localhost", "root", "123456", "etherscan_db")
        cursor = db.cursor()
        results = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
        except:
           print "Error: unable to fecth data"

        # 关闭数据库连接
        db.close()
        return results

    # 把字符串转成datetime
    @staticmethod
    def string_toDatetime(string):
        return datetime.datetime.strptime(string, "%b-%d-%Y %I:%M:%S %p").strftime("%Y-%m-%d %H:%S:%M")
