"""
demo docstring
"""
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def test_name(request):
    """
    demo docstring
    :return:
    """
    return request.node.name

@pytest.fixture
def new_page(test_name):
    """
    demo docstring
    :param test_name:
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=1000)
        context = browser.new_context()
        context.tracing.start(
            name=f"{test_name} context",
            title=f"{test_name} title",
            screenshots=True,
            snapshots=True,
            sources=True
        )
        page = context.new_page()
        page.set_viewport_size({"width": 1000, "height": 800})

        yield page

        context.tracing.stop(path=f"logs/{test_name}_trace.zip")
        browser.close()
