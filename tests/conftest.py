import pytest
from selenium import webdriver
import requests

from urls.urls import MainPageURL, Endpoints
from data.ingredients import Ingredients
from pages.main_page import MainPage, HeaderMainPage
from pages.login_page import LoginPage
from data.data import UserData


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(MainPageURL.MAIN_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(MainPageURL.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    payload = UserData.create_correct_user_data()
    response = requests.post(MainPageURL.MAIN_URL + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    header = {'Authorization': token}
    requests.delete(MainPageURL.MAIN_URL + Endpoints.DELETE_USER, headers=header)


@pytest.fixture
def create_new_order(create_user):
    token = create_user[1].json()['accessToken']
    header = {"Authorization": token}
    ingredients = Ingredients.correct_ingredients_data
    response = requests.post(MainPageURL.MAIN_URL + Endpoints.CREATE_ORDER, headers=header, data=ingredients)
    return response.json()['order']['number']


@pytest.fixture
def login_user(driver, create_user):
    user_data = create_user[0]
    header_page = HeaderMainPage(driver)
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    header_page.click_on_personal_profile_button_in_header()
    login_page.authorization(user_data['email'], user_data['password'])
    main_page.wait_place_order_button_visible()
