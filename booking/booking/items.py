# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    hotel_type = scrapy.Field()
    expedia_id = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    price_un = scrapy.Field()
    price = scrapy.Field()
    star_rating = scrapy.Field()
    review_score = scrapy.Field()
    number_of_reviews = scrapy.Field()
    number_of_rooms = scrapy.Field()
    uri = scrapy.Field()
