from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def wait_loading_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def send_keys_into_field(self, locator, text):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def click_on_button(self, locator):
        element = self.wait_loading_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def check_element(self, locator):
        self.wait_loading_element(locator)
        return self.driver.find_element(*locator)

    def get_text(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def drag_drop(self, element_first, element_second):
        ingredient = self.check_element(element_first)
        basket = self.check_element(element_second)
        drag_and_drop(self.driver, ingredient, basket)

    def check_is_element_not_visible(self, locator):
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_text_from_locator(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def click_after_wait(self, locator):
        target_to_click = self.wait_loading_element(locator)
        target_to_click.click()
