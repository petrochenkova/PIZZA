from os import path

import pytest
from loguru import logger
from playwright.sync_api import Page

from pages.basket_modal import BasketModal
from pages.pizza_modal import PizzaModal
from pages.start_page import StartPage


@pytest.fixture()
def start_page(page: Page) -> StartPage:
    return StartPage(page)


@pytest.fixture()
def pizza_modal(page: Page) -> PizzaModal:
    return PizzaModal(page)


@pytest.fixture()
def basket_modal(page: Page) -> BasketModal:
    return BasketModal(page)


@pytest.fixture()
def basedir():
    basedir = path.dirname(path.abspath(__file__))
    return basedir


@pytest.fixture()
def open_start_page(page: Page, start_page):
    try:
        logger.info("Открытие 'https://dodopizza.ru/'")
        url = "https://dodopizza.ru/"
        page.goto(url)
        start_page.moscow_button.first.click()
        assert page.url == "https://dodopizza.ru/moscow"
        page.wait_for_load_state()
    except Exception as e:
        print(e)
        logger.info("Скриншот падения теста")
        page.screenshot(type='jpeg', path="screenshots/failed_open_start_page.jpeg")
