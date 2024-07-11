import pytest
import allure

from pages.main_page import HeaderMainPage
from pages.order_feed_page import OrderFeedPage
from helpers.helpers import Order
from locators.locators import OrderFeedLocators


class TestOrderFeedPage:

    @allure.title('Проверка, что при нажатии на заказ открывается информационное окно')
    @allure.description('''
   1. Перейдите на главную страницу;
   2. Нажмите на кнопку подачи заказа;
   3. Нажмите на кнопку заказать;
   4. Убедитесь, что информационное окно открыто
    ''')
    def test_check_info_window(self, driver):
        header = HeaderMainPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_order_feed_button_in_header()
        feed_order.click_on_order()
        assert feed_order.check_order_info()

    @allure.title('Проверка, что после увеличения количества новых заказов за всё время и за сегодня, счетчик увеличивается')
    @allure.description('''
   1. Создайте пользователя;
   2. Перейдите на главную страницу;
   3. Войдите в систему пользователя;
   4. Перейдите на страницу выдачи заказов;
   5. Получите текущее количество счетчиков;
   6. Запросите заказ;
   7. Проверьте, увеличился ли счетчик;
   8. Удалите пользователя
    ''')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.counter_of_daily_orders,
                                         OrderFeedLocators.counter_of_total_orders])
    def test_order_counter_updated(self, driver, create_user, login_user, counter):
        order = Order()
        feed_order = OrderFeedPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_order_feed_button_in_header()
        current_counter = int(feed_order.check_orders_counter(counter))
        order.create_order(create_user)
        updated_counter = int(feed_order.check_orders_counter(counter))
        assert updated_counter > current_counter

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description("""
   1. Создайте пользователя;
   2. Перейдите на главную страницу;
   3. Войдите в систему пользователя;
   4. Перейдите на страницу подачи заказов;
   5. Получите список выполняемых заказов;
   6. Получите список оформленных заказов;
   7. Убедитесь, что оформленный заказ находится в списке "В работе";
   8. Удалите пользователя
    """)
    def test_check_order_by_user_in_progress(self, driver, create_user, login_user):
        order = Order()
        header = HeaderMainPage(driver)
        order_feed = OrderFeedPage(driver)
        header.click_on_order_feed_button_in_header()
        order.create_order(create_user)
        orders_in_progress = order_feed.get_orders_in_progress()
        user_order = str(order.get_user_orders(create_user))
        assert user_order in orders_in_progress

    @allure.title('Проверка, что заказы из "Истории заказов" отображаются на странице "Лента заказов"')
    @allure.description('''
   1. Создайте пользователя;
   2. Создайте заказ;
   3. Войдите в систему пользователя;
   4. Перейдите на главную страницу;
   5. Получите заказы пользователя;
   6. Получите список заказов в ленте заказов;
   7. Убедитесь, что заказ пользователя отображается в ленте заказов;
   8. Удалите пользователя
    ''')
    def test_check_order_by_user_appears_in_history(self, driver, create_user, create_new_order, login_user):
        order = Order()
        feed_order = OrderFeedPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_order_feed_button_in_header()
        user_order = str(order.get_user_orders(create_user))
        history_of_orders = feed_order.get_history_of_orders()
        assert user_order in history_of_orders
