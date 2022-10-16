from selenium.webdriver.common.by import By

# url страницы регистрации
url_registration = "https://stellarburgers.nomoreparties.site/register"
# url страницы входа
url_login = "https://stellarburgers.nomoreparties.site/login"
# url домашней страницы
url_home = "https://stellarburgers.nomoreparties.site/"
# url профиля
url_profile = "https://stellarburgers.nomoreparties.site/account/profile"
# url страницы восстановления
url_forgot_password = "https://stellarburgers.nomoreparties.site/forgot-password"

# Форма регистрации
# Поле "Имя"
input_name_registration = (By.XPATH, ".//form/fieldset[1]/div/div/input")
# Поле "Email"
input_email_registration = (By.XPATH, ".//form/fieldset[2]/div/div/input[@name='name']")
# Поле "Пароль"
input_password_registration = (By.XPATH, ".//*[@class='input pr-6 pl-6 input_type_password input_size_default']/input")
# Кнопка "Зарегистрироваться"
button_register = (By.XPATH, ".//form/button[text()='Зарегистрироваться']")
# Кнопка "Войти
link_login = (By.CLASS_NAME, "Auth_link__1fOlj")
# Ошибка пароля
password_error = (By.CLASS_NAME, "input__error")

# Форма входа
# Кнопка "Войти"
button_login = (By.XPATH, ".//form/button[text()='Войти']")
# Поле "Email"
input_email_login = (By.XPATH, ".//input[@name='name']")
# Поле "Пароль"
input_password_login = (By.XPATH, ".//input[@type= 'password']")
# Логотип
logo = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
# Кнопка-ссылка "Зарегистрироваться"
link_register = (By.XPATH, ".//a[@href='/register']")
# Кнопка-ссылка "Восстановить пароль"
link_recover_password = (By.XPATH, ".//a[@href='/forgot-password']")

# Домашняя страница
# Кнопка "Войти в аккаунт"
button_sign_in = (By.CSS_SELECTOR, "button.button_button__33qZ0")
# Кнопка "Личный кабинет"
button_account = (By.XPATH, ".//nav/a[@href='/account']")
# Кнопка "Конструктор"
button_constructor = (By.XPATH, ".//p[text()='Конструктор']")
# Таб Булки
tab_bun = (By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Булки']")
is_selected_tab_bun = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text() = 'Булки']")
# Таб Соусы
tab_sauces = (By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']")
is_selected_tab_sauces = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text() = 'Соусы']")
# Таб Начинки
tab_stuffing = (By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Начинки']")
is_selected_tab_stuffing = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text() = 'Начинки']")

# Профиль пользователя
# Поле Логин
input_login = (By.XPATH, ".//li[@class='Profile_profileListItem__2th0t mb-6'][2]//input")
# Кнопка Выход
button_logout = (By.XPATH, ".//button[text()='Выход']")
