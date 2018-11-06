# -*- coding: utf-8 -*-
import scrapy


class QuotesspiderSpider(scrapy.Spider):
    name = 'quotesSpider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # pass
        quotes=response.xpath("//div[@class='quote']//span[@class='text']/text()",\
            "//div[@class='quote']//span//small[@class='author']/text()").extract()
        author=response.xpath("//div[@class='quote']//span//small[@class='author']/text()").extract()
        yield {'Quotes are here': quotes}
        yield{'Authors are here':author}
