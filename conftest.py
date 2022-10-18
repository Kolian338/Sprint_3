import random as r
import pytest
from selenium import webdriver
from tests.elements import *


# Фикстура для создания  и закрытия драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# фикстура, которая создает и регистрирует пользователя
@pytest.fixture
def user(driver):
    user = User()

    # Регистрация со стачиными данными
    driver.get(url_registration)
    driver.find_element(*input_name_registration).send_keys(user.name)
    driver.find_element(*input_email_registration).send_keys(user.email)
    driver.find_element(*input_password_registration).send_keys(user.password)
    driver.find_element(*button_register).click()

    return user


# Генератор почты
def email_generate():
    number = r.randint(000, 999)
    email = f"safonov_nikolai_03_{number}@yandex.ru"

    return email


# Функция которая создает объет Пользователь
class User:
    def __init__(self, name='Николай', password='123456'):
        self.name = name
        self.email = email_generate()
        self.password = password
