from selenium.webdriver.common.by import By


class Cart:
    def __new__(cls, *args, **kwargs):
        return super(Cart, cls).__new__(cls, *args, **kwargs)

    def navigate_to_cart(self, driver):
        cart = driver.find_element(By.ID, "cartur")
        cart.click()

    def navigate_to_place_order(self, driver):
        # verify that page is looking at cart
        placeorder = driver.find_element(By.XPATH, '//button[text()="Place Order"]')
        placeorder.click()

        name = driver.find_element(By.ID, 'name')
        name.send_keys("Afshan Ejaz")

        country = driver.find_element(By.ID, 'country')
        country.send_keys("USA")

        city = driver.find_element(By.ID, 'city')
        city.send_keys("Dallas")

        card = driver.find_element(By.ID, 'card')
        card.send_keys("0123456789")

        month = driver.find_element(By.ID, 'month')
        month.send_keys("June")

        year = driver.find_element(By.ID, 'year')
        year.send_keys("2022")

        closebutton = driver.find_element(By.XPATH, '//div[button[text()="Purchase"]]/button[text()="Close"]')
        closebutton.click()

    def delete_one_item(self, driver):
        # Enhancement: verify that page is looking at cart
        deleteitem = driver.find_element(By.XPATH, '(//a[text()="Delete"])[1]')
        deleteitem.click()

    def delete_x_items(self, driver, number_of_items):
        # Enhancement: verify that page is looking at cart
        for _ in range(number_of_items):
            self.delete_one_item(driver)
