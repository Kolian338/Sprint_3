from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements import *


# Переход к разделу Булки
def test_go_to_section_buns_click_to_buns_tab_buns_section_is_selected(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).is_displayed()
    driver.find_element(*button_sign_in).click()

    # Ожидание загрузки домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Нажать на таб Соусы
    driver.find_element(*tab_sauces).is_displayed()
    driver.find_element(*tab_sauces).click()
    # Нажать на таб Булки
    driver.find_element(*tab_bun).is_displayed()
    driver.find_element(*tab_bun).click()
    # Проверка что таб выбран
    assert driver.find_element(*is_selected_tab_bun).is_displayed()


# Переход к разделу Соусы
def test_go_to_section_sauces_click_to_sauces_tab_sauces_section_is_selected(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).is_displayed()
    driver.find_element(*button_sign_in).click()

    # Ожидание загрузки домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Нажать на таб Соусы
    driver.find_element(*tab_sauces).is_displayed()
    driver.find_element(*tab_sauces).click()
    # Проверка что таб выбран
    assert driver.find_element(*is_selected_tab_sauces).is_displayed()


# Переход к разделу Начинки
def test_go_to_section_stuffing_click_to_stuffing_tab_stuffing_section_is_selected(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).is_displayed()
    driver.find_element(*button_sign_in).click()

    # Ожидание загрузки домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Нажать на таб Соусы
    driver.find_element(*tab_stuffing).is_displayed()
    driver.find_element(*tab_stuffing).click()
    # Проверка что таб выбран
    assert driver.find_element(*is_selected_tab_stuffing).is_displayed()
