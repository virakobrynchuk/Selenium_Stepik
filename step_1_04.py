from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/find_xpath_form")
elements = browser.find_elements_by_css_selector('[type="text"]')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_xpath("""//form/div/button[@class="btn"][ @type="submit"]""")
button.click()

time.sleep(12)

browser.quit()

