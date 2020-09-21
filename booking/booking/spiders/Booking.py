import scrapy
from booking.items import BookingItem
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response
from statistics import mean 
import datetime

class BookingSpider(scrapy.Spider):
    name = 'booking'
    allowed_domains = ['booking.com']
    site_url = "https://www.booking.com/index.en-gb.html"

    def __init__(self, *args, **kwargs):
        super(BookingSpider, self).__init__(*args, **kwargs)
        self.city  = kwargs.get('city')
        self.date  = kwargs.get('date') # 09/20/2020
        self.date  = datetime.datetime.strptime(self.date, '%m/%d/%Y')

    def start_requests(self):
        yield scrapy.Request(self.site_url, self.parse)

    def parse(self, response):
        checkin  = self.date
        checkout = self.date + datetime.timedelta(days=1)

        data = {
            "ss": getattr(self, 'location', self.city),
            "checkin_month": getattr(self, 'month_in', str(checkin.month).zfill(2)),
            "checkin_monthday": getattr(self, 'day_in', str(checkin.day).zfill(2)),
            "checkin_year": getattr(self, 'year_in', str(checkin.year)),
            "checkout_month": getattr(self, 'month_out', str(checkout.month).zfill(2)),
            "checkout_monthday": getattr(self, 'day_out', str(checkout.day).zfill(2)),
            "checkout_year": getattr(self, 'year_out', str(checkout.year)),
            "no_rooms": getattr(self, 'rooms', '1'),
            "group_adults": getattr(self, 'adults', '1'),
            "group_children": getattr(self, 'children', '0'),
            "selected_currency": getattr(self, 'selected_currency', 'USD')
        }
        print(data)
        yield scrapy.FormRequest.from_response(
            response=response,
            formid="frm",
            formdata=data,
            callback=self.get_hotels,
        )

    def get_hotels(self, response):

        for hotel_url in response.css("div#hotellist_inner div.sr_item a.hotel_name_link ::attr(href)"):
            yield response.follow(hotel_url.extract(), callback=self.parse_hotel)


        next_page = response.css("a.paging-next ::attr(href)")
        if next_page:
            url = next_page[0].extract()
            yield response.follow(url, callback=self.get_hotels)


    def parse_hotel(self, response):
        #open_in_browser(response)
        #from IPython import embed; embed()

        uri        = response.url
        expedia_id = response.xpath(
                        '//div[@id="wrap-hotelpage-top"]/form[@id="top-book"]/input[@name="hotel_id"]/@value'
                    ).extract_first()
        hotel_type = response.css("#hp_hotel_name span ::text").extract_first() 
        hotel_name = response.css("#hp_hotel_name ::text").extract()[-1].strip()
        hotel_lat, hotel_lng = response.css("#hotel_address").attrib['data-atlas-latlng'].split(",")

        review_score = response.css("div.bui-review-score.c-score > div.bui-review-score__badge ::text").extract_first() 
        review_count = response.css("div.bui-review-score.c-score > div.bui-review-score__content > div.bui-review-score__text ::text").extract_first()
        
        if review_count:
            review_count = review_count.strip().split(" ")[0]
        else:
            review_count = "0"

        star_rating  = len(response.css("span.bui-rating__item")) 
        
        un, rooms_prices = self.get_prices(response.css("div.bui-price-display__value ::text").extract())

        rooms = response.css("#hprt-table")[0].css("tr") 
        rooms_count = len(rooms)-1
        
        yield BookingItem(
                name = hotel_name,
                hotel_type = hotel_type,
                expedia_id = expedia_id,
                lat = hotel_lat,
                lng = hotel_lng,
                price = rooms_prices,
                price_un = un,
                star_rating = star_rating,
                review_score = review_score,
                number_of_reviews = review_count,
                number_of_rooms = rooms_count,
                uri = uri)
    
    def get_prices(self, all_prices):
        un = 'US$'
        prices = []

        for p in all_prices:
            price = p.replace("\n", "").replace("US$", "")
            price = float(price.replace(",", ""))
            prices.append(price)

        return [un, mean(prices)]