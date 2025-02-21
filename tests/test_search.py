"""
demo docstring
"""
from pages.search_page import SearchPage


def test_search(new_page):
    """
    demo docstring
    :param new_page:
    :return:
    """
    search_page = SearchPage(new_page)
    search_page.navigate()
    search_page.search("Al Bundy")
    search_page.validate_gpt_button()


def test_search_logo(new_page):
    """
    demo docstring
    :param new_page:
    :return:
    """
    search_page = SearchPage(new_page)
    search_page.validate_logo()
