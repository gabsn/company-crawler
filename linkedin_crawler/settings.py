# coding: utf-8

import os

SETTINGS_PATH = os.path.dirname(os.path.realpath(__file__))

BOT_NAME = 'Spiderman'

SPIDER_MODULES = ['linkedin_crawler.spiders']
NEWSPIDER_MODULE = 'linkedin_crawler.spiders'

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'linkedin_crawler.middlewares.RotateUserAgentMiddleware': 400,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'linkedin_crawler.pipelines.MongoDBPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED=True
# The initial download delay
AUTOTHROTTLE_START_DELAY=2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=4
# Average number of requests Scrapy should be sending in parallel to remote websites.
AUTOTHROTTLE_TARGET_CONCURRENCY=2
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=True

# Never set a download delay lower than DOWNLOAD_DELAY.
DOWNLOAD_DELAY=0.25

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0"

# Ignore robots.txt
ROBOTSTXT_OBEY = False

# MongoDB config
MONGODB = {
        'username': 'gmarignier',
        'password': 'xZX7Tb4xkFSrAf8w',
        'host': 'mongodb.services.dev.mp.mo.sap.corp',
        'db': 'gmarignier_openweb',
        'port': 27017
}

# Retry request if a 999 received
RETRY_TIMES = 5 
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 999]

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
#DOWNLOAD_DELAY=2

# FEED_FORMAT = 'json'
# FEED_URI = '/home/gmarignier/workspace/linkedin/extract.json'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=8
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'linkedin.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
