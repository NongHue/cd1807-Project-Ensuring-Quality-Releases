# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime


def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')

# Start the browser and login with standard_user
def login(user, password):
    print(timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print(timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    # login
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))
    return driver

def add_cart(driver, n_items):
    print (timestamp() +'Test: adding items to cart')
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element_by_css_selector(element).click()  
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()  
        product = driver.find_element_by_css_selector('.inventory_details_name.large_size').text  
        print(timestamp() + product + " added to shopping cart.") 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()  
    print(timestamp() + '{:d} items are all added to shopping cart successfully.'.format(n_items))

def remove_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        product = driver.find_element_by_css_selector('.inventory_details_name.large_size').text
        print(timestamp() + product + " removed from shopping cart.") 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items are all removed from shopping cart successfully.'.format(n_items))

def add_cart_check(driver, n_items):
    print (timestamp() +'Test: adding items to cart for check out')
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element_by_css_selector(element).click()  
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click() 
        product = driver.find_element_by_css_selector('.inventory_details_name.large_size').text  
        print(timestamp() + product + " added to shopping cart.")  
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()  
    print(timestamp() + '{:d} items are all added to shopping cart successfully ready checkout.'.format(n_items))

def check_out(driver):
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.find_element_by_css_selector('.shopping_cart_badge').click()  
    driver.find_element_by_css_selector('#checkout').click() 
    driver.find_element_by_css_selector("input[id='first-name']").send_keys('Hue')
    driver.find_element_by_css_selector("input[id='last-name']").send_keys('Nong')
    driver.find_element_by_css_selector("input[id='postal-code']").send_keys('98501')
    driver.find_element_by_css_selector('#continue').click() 
    driver.find_element_by_css_selector('#finish').click() 
    status_check = driver.find_element_by_css_selector('.complete-header').text
    print(timestamp() + status_check + " .Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    driver.find_element_by_css_selector('#back-to-products').click()  

if __name__ == "__main__":
    N_ITEMS = 6
    TEST_USERNAME = 'standard_user'
    TEST_PASSWORD = 'secret_sauce'
    driver = login(TEST_USERNAME, TEST_PASSWORD)
    add_cart(driver, N_ITEMS)
    remove_cart(driver, N_ITEMS)
    add_cart_check(driver, N_ITEMS)
    check_out(driver)
    print(timestamp() + 'Selenium tests are all successfully completed!')
