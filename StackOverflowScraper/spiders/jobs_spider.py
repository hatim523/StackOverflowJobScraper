import scrapy
import w3lib.html

from StackOverflowScraper.automation.url_generator import URLGenerator
from StackOverflowScraper.items import JobPostItem
from StackOverflowScraper.settings import DEFAULT_JOB_POST_URL
from StackOverflowScraper.spiders.helpers import get_next_button_link


class JobSpider(scrapy.Spider):
    name = 'job_spider'

    def __init__(self, skill=None, location=None, **kwargs):
        self.default_job_post_url = DEFAULT_JOB_POST_URL
        self.generated_url = None

        url_generator = URLGenerator(stop_on_error=True)
        if skill is not None or location is not None:
            self.generated_url = url_generator.get_url_for_query(skill,
                                                                 location)

        super().__init__(**kwargs)

    def start_requests(self):
        if self.generated_url is None:
            print("Working on default url")
            yield scrapy.Request(url=self.default_job_post_url,
                                 callback=self.parse)
        else:
            print("Working on generated url")
            yield scrapy.Request(url=self.generated_url,
                                 callback=self.parse)

    def parse(self, response, **kwargs):
        job_posts = response.css(".stretched-link::attr(href)").getall()

        print(f"Found: {len(job_posts)} job posts")
        for post in job_posts:
            print(f"Looking for post: {post}")
            yield response.follow(post, callback=self.parse_job_info)

        next_page = get_next_button_link(response)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_job_info(self, response, **kwargs):
        job_title = response.css(".sticky\:mb2 .fc-black-900::text").get()
        print(f"{job_title = }")
        company = response.css(".sticky\:sm\:fs-caption "
                               ".fc-black-700::text").get()
        if company is None:
            company = response.css("._up-and-out::text").get()

        company_logo = response.css(".s-avatar--image::"
                                    "attr(src)").getall()
        company_logo = company_logo[0] if company_logo else None

        description = response.css(".mb32.fc-medium div").get()
        description = w3lib.html.remove_tags(description).strip()

        about = response.css(".sm\:fd-column.fc-medium").get()
        about = w3lib.html.remove_tags(about).strip()

        location = response.css(".sticky\:sm\:fs-caption "
                                ".fc-black-500::text").get().strip()
        skills_required = response.css("#overview-items "
                                       ".no-tag-menu::text").getall()

        perks = response.css(".sticky\:fold-up span::text").getall()

        yield JobPostItem(
            job_title=job_title.strip(),
            company=company.strip(),
            company_logo=company_logo,
            description=description,
            about=about,
            location=location,
            skills_required=skills_required,
            job_link=response.url,
            perks=perks,
        )
