from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() 

browser.get('https://www.amazon.com/')
time.sleep(1)
search_input = browser.find_element_by_css_selector('input[type="text"]')
search_input.send_keys('samsung galaxy s22')
time.sleep(1)
search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()
product_1 = browser.find_element_by_css_selector('span[class*="a-size-medium a-color-base a-text-normal"]')
product_1.click()
amazon_price = 410.77

browser.get('https://www.ebay.com')
navigate_input = browser.find_element_by_css_selector('input[type="text"]')
navigate_input.send_keys('samsung galaxy s22')
navigate_btn = browser.find_element_by_css_selector('input[type="submit"]')
navigate_btn.click()
model = browser.find_element_by_css_selector('span[class*="cbx"]')
model.click()
time.sleep(1)
product_2 = browser.find_element_by_xpath('//*[@id="srp-river-results"]')
product_2.click()
ebay_price = 396.16
if amazon_price > ebay_price:
    print('Test Passed')
else:
    print('Test Failed')    
browser.quit()