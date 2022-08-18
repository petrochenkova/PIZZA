import time
from random import randrange

from loguru import logger


def test_add_two_pizzas(page, open_start_page, start_page, pizza_modal, basket_modal, basedir):
    try:
        logger.info("Добавление двух случайных пицц в корзину")
        index1 = randrange(4, 34)
        start_names_list = []
        start_names_list.append(start_page.name_of_random_pizza(index1))
        start_page.open_random_pizza(index1)
        price1 = pizza_modal.price_on_button.inner_text()
        pizza_modal.add_to_basket_button.click()
        index2 = randrange(4, 34)
        while index1 == index2:
            index2 = randrange(4, 34)
        start_names_list.append(start_page.name_of_random_pizza(index2))
        start_page.open_random_pizza(index2)
        price2 = pizza_modal.price_on_button.inner_text()
        pizza_modal.add_to_basket_button.click()
        logger.info("Проверка счетчика корзины")
        time.sleep(0.5)
        assert start_page.basket_quantity.inner_text() == "2"
        logger.info("Открытие корзины")
        start_page.basket_button.click()
        logger.info("Проверка соответствия названий пицц в главном меню к названиям пицц в корзине")
        basket_names_list = basket_modal.names_of_pizzas.all_inner_texts()
        assert start_names_list.sort() == basket_names_list.sort()
        logger.info("Проверка итоговой суммы заказа")
        total_price_on_basket = basket_modal.total_price_of_basket()
        total_price_on_start_page = int(price1) + int(price2)
        assert int(total_price_on_start_page) == int(total_price_on_basket)
        logger.info("Скриншот успешного выполнения теста")
        page.screenshot(path=f"{basedir}/screenshots/success_add_two_pizzas.jpeg")
    except Exception as e:
        print(e)
        logger.info("Скриншот падения теста")
        page.screenshot(path=f"{basedir}/screenshots/failed_add_two_pizzas.jpeg")
