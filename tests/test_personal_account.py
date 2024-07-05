import allure

from urls.urls import URLS, MainPageURL
from pages.main_page import HeaderMainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalProfilePage


class TestPersonalProfilePage:

    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    @allure.description("""
  1. Создайте пользователя;
  2. Перейдите на главную страницу;
  3. Войдите в систему пользователя;
  4. Нажмите на кнопку "Личный кабинет";
  5. Убедитесь, что отображается форма страницы личного профиля;
  6. Удалите пользователя
    """)
    def test_go_to_personal_profile_page(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        personal_profile = PersonalProfilePage(driver)
        header.click_on_personal_profile_button_in_header()
        assert personal_profile.check_personal_profile_visible()
        assert personal_profile.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_personal_profile)

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('''
   1. Создайте пользователя;
   2. Перейдите на главную страницу;
   3. Войдите в систему пользователя;
   4. Нажмите на кнопку "Личный кабинет";
   5. Нажмите на кнопку "Отправить заявку";
   6. Убедитесь, что форма отправки заявки отображена;
   7. Удалите пользователя
    ''')
    def test_go_to_order_feed_page(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        personal_profile = PersonalProfilePage(driver)
        header.click_on_personal_profile_button_in_header()
        personal_profile.click_on_orders_history_button()
        assert personal_profile.check_order_history_form()
        assert personal_profile.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_order_history)

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('''
   1. Создайте пользователя;
   2. Перейдите на главную страницу;
   3. Войдите в систему пользователя;
   4. Нажмите на кнопку "Личный кабинет";
   5. Нажмите на кнопку "Выход";
   6. Убедитесь, что выход завершен успешно;
   7. Удалите пользователя
    ''')
    def test_exit_from_personal_profile(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        login_page = LoginPage(driver)
        personal_profile = PersonalProfilePage(driver)
        header.click_on_personal_profile_button_in_header()
        personal_profile.click_on_exit_button()
        assert login_page.check_presence_of_auth_form()
        assert login_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_login)