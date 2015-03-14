from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from blog_spider.select_result import list_first_item,strip_null,deduplication,clean_url
from blog_spider.items import BlogSpiderItem
from scrapy.spider import Spider
from scrapy.spider  import BaseSpider

class blogSpider1(BaseSpider):
    """docstring for blogSpider"""
    name = "blogSpider1"
    allowed_domains = {'jobbole.com'}
    start_urls = {
        'http://blog.jobbole.com/all-posts/page/20/'
    }

    def parse(self, response):
        next_page = list_first_item(response.xpath(u'//a[@class="next page-numbers"]/@href').extract())
        if next_page:
            next_page = clean_url(response.url,next_page,response.encoding)
            yield Request(url=next_page, callback=self.parse)
            print next_page
        for detail_page in response.xpath(u'//a[@class="meta-title"]/@href').extract():
            if detail_page:
                detail_page = clean_url(response.url,detail_page,response.encoding)
                yield Request(url=detail_page, callback=self.parse_detail)

    def parse_detail(self, response):
        blog_item = BlogSpiderItem()
        blog_item['title'] = response.xpath(u'//div[@class="entry-header"]/h1/text()').extract()
        blog_item['url'] = response.url
        blog_item['content'] = response.xpath(u'//div[@class="entry"]/*/text()').extract()
        yield blog_item
        
# class blogSpider(RedisSpider):
#     """docstring for blogSpider"""
#     name = "blogSpider"
#     # allowed_domains = {'jobbole.com'}
#     start_urls = {
#         'http://blog.sina.com.cn/',
#     }

#     def parse(self, response):
#         next_page = list_first_item(response.xpath(u'*/@href').extract())
#         if next_page:
#             next_page = clean_url(response.url,next_page,response.encoding)
#             print next_page
#             yield Request(url=next_page, callback=self.parse)

#         for detail_page in response.xpath(u'//div[class="blog_title"]/a/@href').extract():
#             if detail_page:
#                 detail_page = clean_url(response.url,detail_page,response.encoding)
#                 print detail_page
#                 yield Request(url=detal_page, callback=parse_detail)

#     def parse_detail(self, response):
#         blog_item = BlogspiderItem()
#         blog_item['title'] = response.xpath(u'//h2[@class="titName SG_txta"]/text()').extract()
#         blog_item['url'] = response.url
#         blog_item['content'] = response.xpath(u'//div[@class="atricalContent"]/*/text()').extract()
#         yield blog_item