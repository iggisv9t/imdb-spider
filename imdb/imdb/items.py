# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    movie_id = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    rec = scrapy.Field()
    genre = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
    date = scrapy.Field()
