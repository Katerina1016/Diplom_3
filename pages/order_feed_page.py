import allure

from locators.locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Получаем номера заказов")
    def get_history_of_orders(self):
        numbers = self.get_text(OrderFeedLocators.order_history_all)
        orders_list = []
        for number in numbers:
            order_number = number.text[2:]
            orders_list.append(order_number)
        return orders_list

    @allure.step('Получаем заказы В работе')
    def get_orders_in_progress(self):
        numbers = self.get_text(OrderFeedLocators.counter_of_orders_in_progress)
        orders_list = []
        for number in numbers:
            order_number = number.text[1:]
            orders_list.append(order_number)
        return orders_list

    @allure.step('Получить сведения счетчика заказов')
    def check_orders_counter(self, locator):
        return self.get_text_from_locator(locator)

    @allure.step('Клик по заказу в ленте заказов')
    def click_on_order(self):
        self.click_after_wait(OrderFeedLocators.order_window_info)

    @allure.step('Проверка отображения окна информации о заказе')
    def check_order_info(self):
        return self.check_element(OrderFeedLocators.orders_info)
