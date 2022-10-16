from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements import *


# Регистрация пользователя с верными данными
def test_registration_correct_email_and_password_the_email_in_the_profile_matches(user, driver):
    driver.get(url_login)

    # Вход
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_login))
    driver.find_element(*input_email_login).send_keys(user.email)
    driver.find_element(*input_password_login).send_keys(user.password)
    driver.find_element(*button_sign_in).click()

    # Переход в личный кабинет
    driver.find_element(*button_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(input_login))
    current_email = driver.find_element(*input_login).get_attribute('value')
    # Проверка почты в профиле с почтой указанной при регистрации
    assert current_email == user.email

    driver.quit()


# Регистрация пользователя с неверным паролем
def test_registration_invalid_password_password_error_is_displayed(driver, user):
    driver.get(url_registration)

    # Вход с неверным паролем
    driver.find_element(*input_name_registration).send_keys(user.name)
    driver.find_element(*input_email_registration).send_keys(user.email)
    driver.find_element(*input_password_registration).send_keys('1')
    driver.find_element(*button_register).click()

    # Проверка ошибки пароля
    error_text = driver.find_element(*password_error).text
    assert error_text == 'Некорректный пароль'

    driver.quit()
