import random as r
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.elements import *


# Фикстура для создания  и закрытия драйвера
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--headless')  # добавили настройку
    #chrome_options.add_argument('--window-size=1920,1080')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки

    yield driver

    driver.quit()


# фикстура, которая создает и регистрирует пользователя
@pytest.fixture
def user(driver):
    user = User()

    # Регистрация со стачиными данными
    driver.get(url_registration)
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url_registration))
    driver.find_element(*input_name_registration).send_keys(user.name)
    driver.find_element(*input_email_registration).send_keys(user.email)
    driver.find_element(*input_password_registration).send_keys(user.password)
    driver.find_element(*button_register).click()

    return user


# Генератор почты
def email_generate():
    number = r.randint(000, 999)
    email = f"safonov_nikolai__{number}@yandex.ru"

    return email


# Функция которая создает объет Пользователь
class User:
    def __init__(self, name='Николай', password='123456'):
        self.name = name
        self.email = email_generate()
        self.password = password
