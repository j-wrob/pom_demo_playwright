"""
demo docstring
"""
from playwright.sync_api import expect


class ImagesPage:
    """
    demo docstring
    :param page:
    :return:
    """

    def __init__(self, page):
        self.page = page
        self.url = "https://bing.com/images"
        self.main_title = page.locator("//div[@class='main-title']")
        self.search_box = page.locator("//input[@id='sb_form_q']")
        self.result_images = page.get_by_label("Image result for Al Bundy's").all()
        self.reject_btn = page.locator("//a[text()='Reject']")

    def navigate(self):
        """
        demo docstring
        :return:
        """
        self.page.goto(url=self.url)

    def search_images(self, text):
        """
        demo docstring
        :return:
        """
        self.search_box.fill(text)
        self.search_box.press("Enter")
        self.reject_btn.click()

    def validate_images_search_results(self):
        """
        demo docstring
        :return:
        """
        for i in self.result_images:
            expect(i).to_be_visible()

    def validate_main_title(self, text):
        """
        demo docstring
        :return:
        """
        expect(self.main_title).to_have_text(text)