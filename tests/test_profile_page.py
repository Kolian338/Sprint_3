from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements import *


# Переход по клику на «Личный кабинет»
def test_go_to_profile_page_click_on_the_account_button_goes_to_the_profile_page(driver, user):
    # Переход на домашнюю страницу
    driver.get(url_home)
    # Переход в личный кабинет
    driver.find_element(*button_account).click()
    # Вход
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login))
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email
    # Проверка что url ведет на страниц профиля
    current_url = driver.current_url
    assert current_url == url_profile

    driver.quit()


# Переход из личного кабинета в конструктор по нажатию на кнопку Конструктор
def test_go_from_profile_page_to_constructor_page_click_on_the_constructor_button_goes_to_the_constructor_page(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login))
    # Нажатие на кнопку Конструктор
    driver.find_element(*button_constructor).click()
    # Проверка что страница конструктора
    current_url = driver.current_url
    assert current_url == url_home

    driver.quit()


# Переход из личного кабинета в конструктор по нажатию на логотип Stellar Burgers
def test_go_from_profile_page_to_constructor_page_click_on_the_logo_goes_to_the_constructor_page(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login))
    # Нажатие на логотип Stellar Burgers
    driver.find_element(*logo).click()
    # Проверка что страница конструктора
    current_url = driver.current_url
    assert current_url == url_home

    driver.quit()


# Выход по кнопке «Выйти» в личном кабинете
def test_logout_click_on_the_logout_button_goes_to_login_page(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login))
    # Нажатие на кнопку Выход
    driver.find_element(*button_logout).click()
    # Проверка что перевело на страницу авторизации
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    current_url = driver.current_url
    assert current_url == url_login

    driver.quit()
