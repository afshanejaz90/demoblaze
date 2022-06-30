import configparser

from selenium import webdriver

from pages.signup import Signup
from pages.homepage import Homepage
from pages.login import Login
from pages.cart import Cart
from pages.logout import Logout


def main():
    # Read configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Using Chrome for testing
    driver = webdriver.Chrome(config['CHROME']['executable'])

    # Change Implicit time to 10s
    driver.implicitly_wait(10)

    # # Navigate to Homepage
    homepage_obj = Homepage()
    homepage_obj.navigate_to_homepage(driver)

    # Sign up task
    signup_obj = Signup()
    signup_obj.sign_up(driver, username=config['DEFAULT']['username'], password=config['DEFAULT']['password'])

    homepage_obj.navigate_to_homepage(driver)

    # Login task
    login_obj = Login()
    login_obj.login(driver, username=config['DEFAULT']['username'], password=config['DEFAULT']['password'])

    # Add two items in card
    homepage_obj.add_two_items_in_cart(driver)


    # Navigate to cart
    cart_obj = Cart()

    # Navigate to Cart
    cart_obj.navigate_to_cart(driver)

    # Navigate to Place order and enter information
    cart_obj.navigate_to_place_order(driver)

    # Delete two items
    cart_obj.delete_x_items(driver, number_of_items=2)

    # Logout
    logout_obj = Logout()
    logout_obj.logout(driver)

    ########################################
    # Login, observe cart and Logout
    ########################################
    # Navigate to home page
    homepage_obj.navigate_to_homepage(driver)

    # Login
    login_obj.login(driver, username=config['DEFAULT']['username'], password=config['DEFAULT']['password'])

    # Navigate to Cart
    cart_obj.navigate_to_cart(driver)

    # Logout
    logout_obj.logout(driver)


    ########################################
    # Pass 2
    ########################################
    # Navigate to home page
    homepage_obj.navigate_to_homepage(driver)

    # Login
    login_obj.login(driver, username=config['DEFAULT']['username'], password=config['DEFAULT']['password'])

    # Add one item in card
    homepage_obj.add_one_item_in_cart(driver)


    # Navigate to cart
    cart_obj.navigate_to_cart(driver)

    # Navigate to Place order and enter information
    cart_obj.navigate_to_place_order(driver)

    # Delete one item from cart
    cart_obj.delete_one_item(driver)

    # Logout
    logout_obj = Logout()
    logout_obj.logout(driver)

    ########################################
    # Login, observe cart and Logout
    ########################################
    # Navigate to home page
    homepage_obj.navigate_to_homepage(driver)

    # Login
    login_obj.login(driver, username=config['DEFAULT']['username'], password=config['DEFAULT']['password'])

    # Navigate to Cart
    cart_obj.navigate_to_cart(driver)

    # Logout
    logout_obj.logout(driver)


if __name__ == "__main__":
    main()
