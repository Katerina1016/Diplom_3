import allure

from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import LocatorsHeader


class HeaderMainPage(BasePage):

    @allure.step("Клик по кнопке Конструктор в шапке главной страницы")
    def click_on_construction_button_in_header(self):
        self.click_on_button(LocatorsHeader.constructor_button)

    @allure.step('Клик по кнопке "Лента заказов" в шапке главной страницы')
    def click_on_order_feed_button_in_header(self):
        self.click_on_button(LocatorsHeader.order_feed_button)

    @allure.step('Клик по кнопке "Личный Кабинет" в шапке главной страницы')
    def click_on_personal_profile_button_in_header(self):
        self.click_on_button(LocatorsHeader.personal_account_button)


class MainPage(BasePage):

    @allure.step('Проверка отображения формы конструктора главной страницы')
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.constructor_form)

    @allure.step('Проверяем отображение ленты заказов')
    def check_order_feed_form(self):
        return self.check_element(MainPageLocators.order_feed_form)

    @allure.step('Клик по кнопке "Войти в аккаунт" на главной странице')
    def click_on_personal_account_button_mainpage(self):
        self.click_on_button(MainPageLocators.personal_account_login_button)

    @allure.step('Клик по флуоресцентной булочке в конструкторе')
    def click_on_bun_in_constructor(self):
        self.click_on_button(MainPageLocators.fluorescent_bun_button)

    @allure.step('Проверяем отображение окна ингредиента')
    def check_bun_info_displayed(self):
        return self.check_element(MainPageLocators.popup_from_ingredient)

    @allure.step('Закрыть окно ингредиента кликом по крестику')
    def close_info_popup(self):
        self.click_on_button(MainPageLocators.cross_icon)

    @allure.step('Проверяем, что окно не отображается/закрыто')
    def check_close_bun_info(self):
        return self.check_is_element_not_visible(MainPageLocators.popup_from_ingredient)

    @allure.step("Проверяем, что кнопка Оформить заказ отображается")
    def wait_place_order_button_visible(self):
        self.wait_loading_element(MainPageLocators.place_order_button)

    @allure.step('Проверяем отображение формы заказа главной страницы')
    def check_order_form_being_displayed(self):
        return self.check_element(MainPageLocators.order_form)

    @allure.step('Добавляем булочку в корзину заказа')
    def bun_add_to_basket(self):
        self.drag_drop(MainPageLocators.fluorescent_bun_button, MainPageLocators.order_basket)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_place_order_button(self):
        self.click_on_button(MainPageLocators.place_order_button)

    @allure.step('Получаем счетчик кол-ва ингредиентов  в заказе')
    def get_number_of_ingredients_in_order(self):
        self.wait_loading_element(MainPageLocators.ingredient_counter)
        return self.get_text_from_locator(MainPageLocators.ingredient_counter)

    @allure.step('Оформляем заказ')
    def create_an_order(self):
        self.bun_add_to_basket()
        self.click_on_place_order_button()
