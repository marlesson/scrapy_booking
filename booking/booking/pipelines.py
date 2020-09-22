# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

class BookingPipeline:
    def open_spider(self, spider):
      pass

    def close_spider(self, spider):
      pass

    def process_item(self, item, spider):
        #...
        item['lat'] = float(item['lat'].strip())
        item['lng'] = float(item['lng'].strip())
        item['number_of_reviews'] = int(item['number_of_reviews'].strip().replace(",",""))

        if item['review_score']:
            item['review_score'] = float(item['review_score'].strip())
        else:
            item['review_score'] = ""

        return item