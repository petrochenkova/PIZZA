from playwright.sync_api import Page


class PizzaModal:

    def __init__(self, page: Page) -> None:
        self.page = page

        # Название пиццы
        self.name_of_pizza = page.locator("(//div[contains(@data-testid,'product__card')]//span)[1]")

        # Кнопка "Маленькая"
        self.small_button = page.locator("[data-testid=\"menu__pizza_size_1\"]")

        # Кнопка "Добавить в корзину"
        self.add_to_basket_button = page.locator("button:has-text('Добавить в корзину за ')")

        # Стоимость в кнопке
        self.price_on_button = page.locator(
            "//div[contains(@data-testid, \"product__card\")]/div[2]/div[2]//span/span[1]")
