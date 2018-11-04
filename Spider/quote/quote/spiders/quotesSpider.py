# -*- coding: utf-8 -*-
import scrapy


class QuotesspiderSpider(scrapy.Spider):
    name = 'quotesSpider'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://http://quotes.toscrape.com//']

    def parse(self, response):
        pass
