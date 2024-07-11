import allure

from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):

    @allure.step('Отправляем почту в поле ввода')
    def send_keys_to_email_field(self, email):
        self.send_keys_into_field(AuthPageLocators.email_input_field, email)

    @allure.step('Отправляем пароль в поле ввода')
    def send_keys_to_password_field(self, password):
        self.send_keys_into_field(AuthPageLocators.password_input_field, password)

    @allure.step('Клик по кнопке "Логин" окна авторизации')
    def click_on_login_button(self):
        self.click_on_button(AuthPageLocators.login_account_button)

    @allure.step('Авторизация')
    def authorization(self, email, password):
        self.send_keys_to_email_field(email)
        self.send_keys_to_password_field(password)
        self.click_on_login_button()

    @allure.step('Клик по кнопке "Восстановить пароль" окна авторизации')
    def click_on_recovery_button(self):
        self.click_on_button(AuthPageLocators.recovery_button)

    @allure.step("Проверяем наличие формы окна авторизации")
    def check_presence_of_auth_form(self):
        return self.check_element(AuthPageLocators.authorization_form)