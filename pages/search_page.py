"""
demo docstring
"""
from playwright.sync_api import expect
import pytest


class SearchPage:
    """
    demo docstring
    :param page:
    :return:
    """

    def __init__(self, page):
        self.page = page
        self.url = "https://bing.com"
        self.search_box = page.locator("//textarea[@id='sb_form_q']")
        self.logo = page.locator("//*[@aria-label='Welcome to Bing Search']")
        self.short_info = page.locator("//span[@class='wpt-ovd']")

    def navigate(self):
        """
        demo docstring
        :return:
        """
        self.page.goto(url=self.url)

    def search(self, text):
        """
        demo docstring
        :return:
        """
        self.search_box.fill(text)
        self.search_box.press("Enter")

    def validate_logo(self):
        """
        demo docstring
        :return:
        """
        self.logo.is_visible()

    def validate_short_info(self, text):
        """
        demo docstring
        :return:
        """
        expect(self.short_info).to_have_text(text)
