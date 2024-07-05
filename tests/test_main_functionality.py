import allure

from urls.urls import URLS, MainPageURL
from pages.main_page import MainPage, HeaderMainPage


class TestMainPage:

    @allure.title('Проверка перехода к конструктору')
    @allure.description("""
    1. Перейдите на главную страницу;
    2. Нажмите на кнопку "Личный кабинета";
    3. Нажмите на кнопку Конструктора;
    4. Проверьте отображение формы конструктора
    """)
    def test_proceeding_to_constructor(self, driver):
        header = HeaderMainPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        header.click_on_construction_button_in_header()
        assert main_page.check_constructor_form() and main_page.get_current_url() == MainPageURL.MAIN_URL

    @allure.title('Проверка перехода к Ленте заказов')
    @allure.description("""
    1. Перейдите на главную страницу;
    2. Нажмите на кнопку выдачи заказа;
    3. Проверьте отображение формы выдачи заказа
    """)
    def test_proceeding_to_order_feed(self, driver):
        header = HeaderMainPage(driver)
        main_page = MainPage(driver)
        header.click_on_order_feed_button_in_header()
        assert main_page.check_order_feed_form() and main_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_feed)

    @allure.title('Проверка всплывающего информационного окна после нажатия на ингредиент')
    @allure.description('''
    1. Перейдите на главную страницу;
    2. Нажмите на флуоресцентную булочку;
    3. Убедитесь, что отображается всплывающее окно с информацией о булочке
    ''')
    def test_check_bun_info_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_in_constructor()
        assert main_page.check_bun_info_displayed()

    @allure.title('Проверка закрытия информационного окна')
    @allure.description('''
    1. Перейдите на главную страницу;
    2. Нажмите на флуоресцентную булочку;
    3. Нажмите на закрытие окна;
    4. Убедитесь, что окно закрыто
    ''')
    def test_check_bun_info_window_closed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_in_constructor()
        main_page.close_info_popup()
        assert main_page.check_close_bun_info()

    @allure.title('Проверка, что счетчик ингредиентов увеличивает количество')
    @allure.description('''
    1. Перейдите на главную страницу;
    2. Положите булочку в корзину;
    3. Убедитесь, что счетчик увеличивается
    ''')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.bun_add_to_basket()
        assert int(main_page.get_number_of_ingredients_in_order()) > 0

    @allure.title('Зарегистрированный пользователь может оформить заказ')
    @allure.description('''
   1. Создайте пользователя;
   2. Перейдите на главную страницу;
   3. Авторизуйтесь как пользователь;
   4. Добавьте булочку в корзину;
   5. Нажмите на кнопку оформить заказ;
   6. Проверьте, видна ли форма заказа;
   7. Удалите пользователя с помощью API.
    ''')
    def test_create_order_by_logged_user(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_construction_button_in_header()
        main_page.create_an_order()
        assert main_page.check_order_form_being_displayed()
