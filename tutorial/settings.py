# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 6
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate, sdch',
   'Accept-Language': 'zh-CN,zh;q=0.9',
   'Connection': 'keep-alive',
   'Cookie': 'BAIDUID=7AEAEE0CD9989941B1C56FBA3CF34BB9:FG=1; BIDUPSID=7AEAEE0CD9989941B1C56FBA3CF34BB9; PSTM=1524104175; BDUSS=jNqSW5RUXdHcERaeFZaaHgxNzZGSVJqazAxZUgzU0tNT3cxc3BicFBRWVNuUDlhQVFBQUFBJCQAAAAAAAAAAAEAAAB1pfpWxKrT6vPjz~4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIP2FoSD9haY; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1524118937,1524121775,1524130312,1524209674; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1524478906; from_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; BDSFRCVID=wlPsJeC626aNgiOAY91tMZI0fNbJ8ETTH6ao-DpZUBMCS9gu41thEG0PDU8g0Kub-mPZogKK3gOTH4nP; H_BDCLCKID_SF=tJIJoIKKfCt3f-opMtTEh4bHjHQ2-P4XKKOLVhr2bPOkeq8CDx-b5bD454QbbhOpBGQAoMoGMnvqeRc2y5jHhnvLhPbbQbovtgT0_n_y-COpsIJMQbAWbT8U5f5EtbOaaKviaKOjBMb1MbrMe6DMej3WDaus-bbfHD5a0RTD5RrJKROvhjRUWfFyyxomtjjNLHRA3D5p5POpfh6LyjbC3hLsjfQqLUkqKGcU3hvT3n5ahf-lXqbChxJQQttjQnohfIkja-KEKR6FSn7TyU45bU47yaOXQTIqJnKJ_KtXf-3bfTrY-4oEb4LHbgT22-usQICJQhcH0KLKVxoMytKhLt0yQJbuXfFeLHnP0K5qbfb1MRjK3PbvQU08KHQnJxrgLDomop5TtUJaeCnTDMRhqt_DXRJyKMnitKv9-pP2aft0hCtlDTLajT3M5pJfetca5C5h0RrjHJO_bpD9QbbkbfJBDR5NbUQ-We6bQh54BxczhUo23tth-JK7yajKLfrya6cR5tTeWPT5VIbIeh7pQT8rKfDOK5OibCrD_DQvab3vOIOTXpO1j-CreGKttT8tJJKjV-b-KRT_jJrTq6_a-n0eqxby26nvQe7eaJ5nJDoToKbo-P5NbMLPy-czB6JNaHrDQ4nKQpP-HqTTjMoOWJ0dXfrGQ53afT6GKl0MLpbWbb0xynoD26-Q-xnMBMPe52OnaIb8LIFKMK0mD5LhDTPW5ptXKJQEKCj-B6rJabC3hM5DKU6qLT5XKGrb2xb90G5ZLb7zyqI5fnbdeqOWDp0njxQA25k8fmnjKlDhXh6OMttw3MonDh8vXH7MJUntKDrGKp6O5hvvhn3O3MAMhlOhDG_DJTKJJRusQb5EHtbHD4cdhnoqbbQH-UnLqbbQLT7Z0l8KtDQH8R3YXUQZej_3XJ6AJP5wKeLOKxbmWIQHDT6eKh6lLxud0NrM-60DbIb4KKJx3UKWeIJo5tKVhq8lhUJiB5JMBan7_nrxfJOKHICmj5KKef5; H_PS_PSSID=1431_21083_18560_22075; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=7',
   'DNT': '1',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 600
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
