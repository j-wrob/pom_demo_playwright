"""
demo docstring
"""
from pages.images_page import ImagesPage


def test_search_images(new_page):
    """
    demo docstring
    :param new_page:
    :return:
    """
    images_page = ImagesPage(new_page)
    images_page.navigate()
    images_page.search_images("Al Bundy's dog")
    images_page.validate_images_search_results()

def test_main_title(new_page):
    """
    demo docstring
    :param new_page:
    :return:
    """
    images_page = ImagesPage(new_page)
    images_page.navigate()
    images_page.validate_main_title()

def test_to_generate_fail(new_page):
    """
    demo docstring
    :param new_page:
    :return:
    """
    images_page = ImagesPage(new_page)
    images_page.navigate()
    images_page.validate_main_title()
    assert False
