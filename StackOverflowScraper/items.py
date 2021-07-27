# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobPostItem(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    company_logo = scrapy.Field()
    location = scrapy.Field()
    skills_required = scrapy.Field()
    perks = scrapy.Field()
    about = scrapy.Field()
    description = scrapy.Field()
    job_link = scrapy.Field()


