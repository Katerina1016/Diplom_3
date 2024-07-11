import allure

from locators.locators import PersonalProfileLocators
from pages.base_page import BasePage


class PersonalProfilePage(BasePage):

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on_button(PersonalProfileLocators.order_history_button)

    @allure.step("Клик по кнопке Выход")
    def click_on_exit_button(self):
        self.click_on_button(PersonalProfileLocators.exit_button)

    @allure.step("Проверяем отображение истории заказов")
    def check_order_history_form(self):
        return self.check_element(PersonalProfileLocators.order_history_form)

    @allure.step('Проверяем отображение формы личного кабинета')
    def check_personal_profile_visible(self):
        return self.check_element(PersonalProfileLocators.profile_form)