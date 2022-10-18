from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements import *


# Вход по кнопке «Войти в аккаунт» на главной
def test_login_by_button_log_in_to_account_correct_email_and_password_the_email_in_the_profile_matches(driver, user):
    driver.get(url_home)
    # Нажатие на кнопку "Войти в аккаунт"
    driver.find_element(*button_sign_in).click()
    # Авторизация
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    # Ожидание поля Логин в профиле
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(input_login))
    # Получение значения из поля Логин
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email


# Вход через кнопку «Личный кабинет»
def test_login_by_button_personal_account_correct_email_and_password_the_email_in_the_profile_matches(driver, user):
    # Переход на домашнюю страницу
    driver.get(url_home)
    # Нажатие на кнопку Личный кабинет
    driver.find_element(*button_account).click()
    # Вход из страницы личного кабинета
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(input_login))
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email


# Вход через кнопку в форме регистрации
def test_login_by_button_login_in_the_registration_form_correct_email_and_password_the_email_in_the_profile_matches(driver, user):
    # Переход на страницу регистрации
    driver.get(url_registration)
    # Вход через кнопку-ссылку "Войти" в форме регистрации
    driver.find_element(*link_login).click()
    WebDriverWait(driver, 15).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(input_login))
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email


# Вход через кнопку в форме восстановления
def test_login_by_button_login_in_the_password_recovery_form_correct_email_and_password_the_email_in_the_profile_matches(driver, user):
    # Переход на страницу восстановления пароля
    driver.get(url_forgot_password)
    # Вход через кнопку-ссылку "Войти" в форме востановления пароля
    driver.find_element(*link_login).click()
    WebDriverWait(driver, 15).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).is_displayed()
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(input_login))
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email
