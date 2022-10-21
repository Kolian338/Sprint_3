from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements import *


# Переход по клику на «Личный кабинет»
def test_go_to_profile_page_click_on_the_account_button_goes_to_the_profile_page(driver, user):
    # Переход на домашнюю страницу
    driver.get(url_home)
    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_email_login)).is_displayed()
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Ждем url домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login)).is_displayed()
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email
    # Проверка что url ведет на страниц профиля
    current_url = driver.current_url
    assert current_url == url_profile


# Переход из личного кабинета в конструктор по нажатию на кнопку Конструктор
def test_go_from_profile_page_to_constructor_page_click_on_the_constructor_button_goes_to_the_constructor_page(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_email_login)).is_displayed()
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Ждем url домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login)).is_displayed()
    # Нажатие на кнопку Конструктор
    driver.find_element(*button_constructor).click()

    # Ждем url домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Проверка что страница конструктора
    current_url = driver.current_url
    assert current_url == url_home


# Переход из личного кабинета в конструктор по нажатию на логотип Stellar Burgers
def test_go_from_profile_page_to_constructor_page_click_on_the_logo_goes_to_the_constructor_page(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_email_login)).is_displayed()
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Ждем url домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login)).is_displayed()
    # Нажатие на логотип Stellar Burgers
    driver.find_element(*logo).click()

    # Ждем url домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Проверка что страница конструктора
    current_url = driver.current_url
    assert current_url == url_home


# Выход по кнопке «Выйти» в личном кабинете
def test_logout_click_on_the_logout_button_goes_to_login_page(driver, user):
    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_email_login)).is_displayed()
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Ждем url домашней страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_home))

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    # Ждем Поле Логин и его отображение
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login)).is_displayed()
    # Нажатие на кнопку Выход
    driver.find_element(*button_logout).is_displayed()
    driver.find_element(*button_logout).click()
    # Проверка что перевело на страницу авторизации
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    current_url = driver.current_url
    assert current_url == url_login
