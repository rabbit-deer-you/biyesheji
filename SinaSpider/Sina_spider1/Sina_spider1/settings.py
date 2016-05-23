# encoding=utf-8
BOT_NAME = 'Sina_spider1'

SPIDER_MODULES = ['Sina_spider1.spiders']
NEWSPIDER_MODULE = 'Sina_spider1.spiders'

RETRY_TIMES = 10
RETRY_HTTP_CODES = [ 500 , 503 , 504 , 400 , 403 , 404 , 408 ,302]

DOWNLOADER_MIDDLEWARES = {
    "Sina_spider1.middleware.UserAgentMiddleware": 401,
    "Sina_spider1.middleware.CookiesMiddleware": 402,
}

ITEM_PIPELINES = ["Sina_spider1.pipelines.MongoDBPipleline"]

DOWNLOAD_DELAY = 2 # 间隔时间
# CONCURRENT_ITEMS = 1000
# CONCURRENT_REQUESTS = 100
REDIRECT_ENABLED = False
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 0
# CONCURRENT_REQUESTS_PER_SPIDER=100
# DNSCACHE_ENABLED = True
# LOG_LEVEL = 'INFO'    # 日志级别
# CONCURRENT_REQUESTS = 70
