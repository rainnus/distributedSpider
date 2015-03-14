# -*- coding: utf-8 -*-

# Scrapy settings for blog_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'blog_spider'

SPIDER_MODULES = ['blog_spider.spiders']
NEWSPIDER_MODULE = 'blog_spider.spiders'

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Schedule requests using a queue (FIFO).
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# Schedule requests using a stack (LIFO).
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'blog_spider.pipelines.BlogSpiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

DOWNLOADER_MIDDLEWARES = {
#    'woaidu_crawler.contrib.downloadmiddleware.google_cache.GoogleCacheMiddleware':50,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    #'blog_spider.downloadermiddleware.rotate_useragent.RotateUserAgentMiddleware':400,
}
# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
LOG_FILE = "logs/scrapy.log"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'blog_spider (+http://www.yourdomain.com)'
