# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import random
#import settings
#from services.mail_sender import ScrapyMailSender
from scrapy import signals
from w3lib.http import basic_auth_header
import env
import logging


# class CustomHttpErrorMiddleware(object):
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings)

#     def __init__(self, settings):
#         self.count_errors = 0
#         self.handle_httpstatus_list = settings.getlist('HTTPERROR_ALLOWED_CODES')

#     def process_spider_input(self, response, spider):
#         if env.PROXY["enable"]:
#             if response.status in self.handle_httpstatus_list:
#                 self.count_errors += 1
#                 logger = logging.getLogger()
#                 logger.error(f"HTTP Error {response.status}")
#             if self.count_errors > 10:
#                 mailer = ScrapyMailSender()
#                 message = f"There is {self.count_errors} errors whith status {response.status}"
#                 mailer.send_email(data=message)
#                 return
#             else:
#                 return


# class CustomProxyMiddleware(object):
#     def process_request(self, request, spider):
#         if env.PROXY["enable"]:
#             url = random.choice(env.PROXY["urls"])
#             request.meta['proxy'] = f"{url}:{env.PROXY['port']}"
#             request.headers['Proxy-Authorization'] = basic_auth_header(
#                 f"{env.PROXY['name']}", f"{env.PROXY['pass']}")

class BookingSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BookingDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
