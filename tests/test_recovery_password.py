import allure

from urls.urls import URLS, MainPageURL
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage
from data.data import UserData


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('''
    1. Перейдите на главную страницу;
    2. Перейдите на страницу личного профиля;
    3. Нажмите на кнопку Восстановить пароль.
    ''')
    def test_recover_password_button(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        assert recovery_page.check_recovery_form()
        assert recovery_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_recovery)

    @allure.title('Проверка, клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description('''
   1. Перейдите на главную страницу;
   2. Перейдите на страницу личного профиля;
   3. Нажмите на кнопку восстановить пароль;
   4. Заполните поле ввода электронной почты;
   5. Нажмите на кнопку восстановить;
   6. Заполните поле ввода пароля;
   7. Нажмите на кнопку Показать пароль.
    ''')
    def test_check_highlighting_of_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        user_data = UserData().create_correct_user_data()
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        recovery_page.send_keys_to_email_field(user_data.get('email'))
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_field_password_is_active(user_data.get('password'))

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('''
    1. Перейдите на главную страницу;
    2. Перейдите на страницу личного кабинета;
    3. Нажмите на кнопку восстановить пароль.;
    4. Заполните адрес электронной почты в поле ввода email;
    5. Нажмите на кнопку Восстановить.
    ''')
    def test_email_input_and_recover_button_click(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        recovery_page.send_keys_to_email_field(UserData().create_correct_user_data()['email'])
        recovery_page.click_on_recovery_button()
        assert recovery_page.save_button_check()
        assert recovery_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_reset_password)
