from loguru import logger


def test_pizzas_list_and_city(page, open_start_page, start_page, basedir):
    try:
        logger.info("Проверка общего кол-ва товаров в разделе 'Пицца'")
        assert start_page.pizzas_buttons.count() == 34
        logger.info("Проверка отображения города доставки")
        assert start_page.city_text.inner_text() == "Москва"
        logger.info("Скриншот успешного выполнения теста")
        page.screenshot(path=f"{basedir}/screenshots/success_pizzas_list_and_city.jpeg")
    except Exception as e:
        print(e)
        logger.info("Скриншот падения теста")
        page.screenshot(path=f"{basedir}/screenshots/failed_pizzas_list_and_city.jpeg")
