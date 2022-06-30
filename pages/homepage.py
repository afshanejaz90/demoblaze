from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Homepage:
    def __new__(cls, *args, **kwargs):
        return super(Homepage, cls).__new__(cls, *args, **kwargs)

    def navigate_to_homepage(self, driver):
        driver.get("https://www.demoblaze.com/")
        driver.get_screenshot_as_file(f'./images/{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.png')

    def click_on_home_toolbar(self, driver):
        home = driver.find_element(By.XPATH, '//a[@class="nav-link"]')
        home.click()

    def add_two_items_in_cart(self, driver):
        self.add_one_item_in_cart(driver)
        self.click_on_home_toolbar(driver)
        self.add_second_item_in_cart(driver)

    def add_second_item_in_cart(self, driver):
        nokia = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, "//a[text()='Nokia lumia 1520']"))
        nokia.click()

        addtocart = driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
        addtocart.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())

        alert = Alert(driver)
        alert.accept()

    def add_one_item_in_cart(self, driver):
        # pause before moving on
        samsung = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CSS_SELECTOR, "a.hrefch"))
        samsung.click()

        addtocart = driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
        addtocart.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())

        alert = Alert(driver)
        alert.accept()
