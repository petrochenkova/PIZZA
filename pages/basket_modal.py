import unidecode as unidecode
from playwright.sync_api import Page


class BasketModal:

    def __init__(self, page: Page) -> None:
        self.page = page

        # Названия пицц
        self.names_of_pizzas = page.locator("//section[@data-testid=\"cart__list\"]//h3")

        # Итоговая сумма корзины
        self.total_price = page.locator("text=Сумма заказа")

    def total_price_of_basket(self):
        total_price = self.total_price.inner_text()
        total_price = unidecode.unidecode(total_price[13:-2]).replace(" ", "")
        return total_price
