import re
from random import randrange

from playwright.sync_api import Page


class StartPage:

    def __init__(self, page: Page) -> None:
        self.page = page

        # Кнопка "Москва"
        self.moscow_button = page.locator(
            "[data-testid=\"locality-selector-popup__big-city-0000002b-0000-0000-0000-000000000000\"]")

        # Кнопка "Корзина"
        self.basket_button = page.locator("[data-testid=\"navigation__cart\"]")
        # Счетчик корзины
        self.basket_quantity = page.locator("[data-testid=\"cart-button__quantity\"]")

        # Кнопки пицц
        self.pizzas_buttons = page.locator("(//section[@id=\"pizzas\"]//article)")

        # Город доставки
        self.city_text = page.locator("[data-testid=\"header__about-slogan-text_link\"]")

        # Кнопки "Выбрать"
        self.choose_button = page.locator(f"(//section[@id=\"pizzas\"]//button)[{randrange(4, 34)}]")

    def open_random_pizza(self, index):
        self.page.wait_for_load_state()
        self.page.locator(f"(//section[@id=\"pizzas\"]//button)[{index + 2}]").click()

    def name_of_random_pizza(self, index):
        self.page.wait_for_load_state()
        name = self.page.locator(
            f"(//section[@id=\"pizzas\"]//div[@data-gtm-id=\"product-title\"])[{index}]").inner_text()
        while name.isalpha() == True:
            return name
        else:
            name = re.sub(r" 🌱", "", name)
            name = re.sub(r" 🌱👶", "", name)
            name = re.sub(r" 🌶️🌶️ ", "", name)
            return name

    def price_on_start_page(self, index):
        full_price = self.page.locator(
            f"(//section[@id=\"pizzas\"]//article[contains(@data-testid, \"menu__meta-product\")]//footer//div)[{index}]").inner_text()
        price = full_price[3:-2]
        return price
