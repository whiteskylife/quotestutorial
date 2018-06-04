# -*- coding: utf-8 -*-
import scrapy
from quotestutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print(response.text)
        # print(response.headers)
