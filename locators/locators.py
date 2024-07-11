from selenium.webdriver.common.by import By


class LocatorsHeader:
    constructor_button = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    order_feed_button = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    personal_account_button = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")


class MainPageLocators:
    order_feed_form = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    constructor_form = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    fluorescent_bun_button = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    cross_icon = (By.XPATH, '//button[contains(@class,"close")]')
    order_form = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    order_basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    ingredient_counter = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    order_number = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    personal_account_login_button = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    popup_from_ingredient = (By.XPATH, "//h2[text()= 'Детали ингредиента']")


class AuthPageLocators:
    authorization_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    email_input_field = (By.XPATH, ".//input[@name = 'name']")
    password_input_field = (By.XPATH, ".//input[@name = 'Пароль']")
    login_account_button = (By.XPATH, "//button[text() = 'Войти']")
    registration_button = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    recovery_button = (By.XPATH, "//a[text() = 'Восстановить пароль']")


class RecoverPageLocators:
    email_input_field = (By.XPATH, ".//input[@name = 'name']")
    recover_button = (By.XPATH, "//button[text() = 'Восстановить']")
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']")
    new_password_input_field = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    code_from_email_input_field = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    show_password_button = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    password_input_field_active = (By.CSS_SELECTOR, ".input.input_status_active")
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")
    recover_form_text = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")


class PersonalProfileLocators:
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']")
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")
    order_history_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
    order_number = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    cancel_button = (By.XPATH, ".//button[text() = 'Отмена']")
    exit_button = (By.XPATH, ".//button[text() = 'Выход']")
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")


class OrderFeedLocators:
    orders_info = (By.XPATH, '//p[text()="Cостав"]')
    title_orders_feed = (By.XPATH, '//h1[text()="Лента заказов"]')
    counter_of_total_orders = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    counter_of_daily_orders = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    counter_of_orders_in_progress = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    order_window_info = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    order_history_all = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
