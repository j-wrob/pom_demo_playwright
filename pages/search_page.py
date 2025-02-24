"""
demo docstring
"""
from playwright.sync_api import expect


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
        self.gpt_btn = page.locator("//span[@id='b_sh_btn_isprt']")

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

    def validate_gpt_button(self):
        """
        demo docstring
        :return:
        """
        expect(self.gpt_btn).to_be_visible()
        expect(self.gpt_btn).to_be_enabled()
