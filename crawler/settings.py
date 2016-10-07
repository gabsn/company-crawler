# coding: utf-8

import os

SETTINGS_PATH = os.path.dirname(os.path.realpath(__file__))

BOT_NAME = 'Spiderman'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

LOG_LEVEL='DEBUG'

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'crawler.middlewares.StatusHandlerMiddleware': 100,
    'crawler.middlewares.RotateUserAgentMiddleware': 400,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'crawler.pipelines.MongoDBPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED=True
# The initial download delay
AUTOTHROTTLE_START_DELAY=2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=4
# Average number of requests Scrapy should be sending in parallel to remote websites.
AUTOTHROTTLE_TARGET_CONCURRENCY=1
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=True

# Never set a download delay lower than DOWNLOAD_DELAY.
DOWNLOAD_DELAY=0.1

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=8
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0"

# Ignore robots.txt
ROBOTSTXT_OBEY = False

# MongoDB config
MONGODB = {
    'host': 'localhost',
    'db': 'company-crawler',
    'port': 27017
}

# Retry request if a 999 received
#RETRY_TIMES = 5 
#RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 999]

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False
