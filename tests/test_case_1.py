from random import randrange

from loguru import logger


def test_add_pizza(page, open_start_page, start_page, pizza_modal, basedir):
    try:
        logger.info("Добавление случайной пиццы в корзину")
        index = randrange(4, 34)
        name_on_start_page = start_page.name_of_random_pizza(index)
        price_on_start_page = start_page.price_on_start_page(index)
        start_page.open_random_pizza(index)
        logger.info("Проверка соответствия наименования пиццы в главном меню к наименованию в модальном окне")
        name_on_modal_page = pizza_modal.name_of_pizza.inner_text()
        assert name_on_start_page == name_on_modal_page
        logger.info("Выбор маленькой пиццы")
        pizza_modal.small_button.click()
        logger.info("Проверка соответствия стоимости пиццы в главном меню к стоимости в модальном окне")
        price_on_modal_page = pizza_modal.price_on_button.inner_text()
        assert price_on_start_page == price_on_modal_page
        logger.info("Добавление в корзину")
        pizza_modal.add_to_basket_button.click()
        logger.info("Проверка счетчика корзины")
        assert start_page.basket_quantity.inner_text() == "1"
        logger.info("Скриншот успешного выполнения теста")
        page.screenshot(path=f"{basedir}/screenshots/success_add_pizza.jpeg")
    except Exception as e:
        print(e)
        logger.info("Скриншот падения теста")
        page.screenshot(path=f"{basedir}/screenshots/failed_add_pizza.jpeg")
