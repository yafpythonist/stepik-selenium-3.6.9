import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_at_least_one_add_to_cart_button_exists(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons), f"Нет кнопок добавления в корзину"
    time.sleep(30)
