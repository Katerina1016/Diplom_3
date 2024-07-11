import allure

from pages.base_page import BasePage
from locators.locators import RecoverPageLocators


class RecoveryPage(BasePage):
    @allure.step('Проверка отображения формы восстановления')
    def check_recovery_form(self):
        return self.check_element(RecoverPageLocators.recover_form_text)

    @allure.step(' Отправляем значение email в поле')
    def send_keys_to_email_field(self, email):
        self.send_keys_into_field(RecoverPageLocators.email_input_field, email)

    @allure.step('Отправляем значение пароля в поле')
    def send_keys_to_password_field(self, password):
        self.send_keys_into_field(RecoverPageLocators.new_password_input_field, password)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_recovery_button(self):
        self.click_on_button(RecoverPageLocators.recover_button)

    @allure.step('Проверка отображения кнопки "Сохранить')
    def save_button_check(self):
        return self.check_element(RecoverPageLocators.save_button)

    @allure.step("Проверка, что поле пароля подсвечивается")
    def check_field_password_is_active(self, password):
        self.send_keys_to_password_field(password)
        self.click_on_button(RecoverPageLocators.show_password_button)
        return self.check_element(RecoverPageLocators.password_input_field_active)
