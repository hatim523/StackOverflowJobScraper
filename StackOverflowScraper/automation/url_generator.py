import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class URLGenerator:
    def __init__(self, stop_on_error=False):
        self.stop_on_error = stop_on_error

        self.driver = None
        self.jobs_parent_page = "https://stackoverflow.com/jobs"

        self.chromedriver_location = os.path.join(os.getcwd(),
                                                  "chromedriver.exe")

        # chromedriver options
        self.options = Options()
        self.options.headless = True

    def start_driver(self):
        self.driver = webdriver.Chrome(self.chromedriver_location,
                                       options=self.options)

    def get_url_for_query(self, skill=None, location=None):
        if skill is None and location is None:
            raise Exception("URLGenerator requires either skill or "
                            "location to generate url for jobs.")

        self.start_driver()

        self.driver.get(self.jobs_parent_page)
        skill is not None and self.enter_skill_query(skill)
        location is not None and self.enter_location_query(location)
        # now search for the entered query
        time.sleep(2)
        self.search_query()
        time.sleep(3)
        current_url = self.driver.current_url

        self.driver.quit()
        return current_url

    def enter_location_query(self, location):
        try:
            self.driver.find_element_by_css_selector(".pac-target-input").\
                send_keys(location)
        except Exception as e:
            print(e)
            if self.stop_on_error:
                raise Exception(e)

    def enter_skill_query(self, skill):
        try:
            self.driver.find_element_by_css_selector(".brr0").send_keys(skill)
        except Exception as e:
            print(e)
            if self.stop_on_error:
                raise Exception(e)

    def search_query(self):
        try:
            self.driver.find_element_by_css_selector(".ws-nowrap.h100").click()
        except Exception as e:
            print(e)
            if self.stop_on_error:
                raise Exception(e)
