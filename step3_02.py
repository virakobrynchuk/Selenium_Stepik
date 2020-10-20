import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_css_selector('.first:required').send_keys("Моя відповідь")
        browser.find_element_by_css_selector('.second:required').send_keys("Моя відповідь")
        browser.find_element_by_css_selector('.third:required').send_keys("Моя відповідь")
        browser.find_element_by_css_selector("button.btn").click()

        self.assertEqual(browser.find_element_by_tag_name("h1").text,
                         "Congratulations! You have successfully registered!")
        browser.quit()

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_css_selector('.first:required').send_keys("Моя відповідь")
        # browser.find_element_by_css_selector('.second:required').send_keys("Моя відповідь")
        browser.find_element_by_css_selector('.third:required').send_keys("Моя відповідь")
        browser.find_element_by_css_selector("button.btn").click()

        self.assertEqual(browser.find_element_by_tag_name("h1").text,
                         "Congratulations! You have successfully registered!")
        browser.quit()


if __name__ == "__main__":
    unittest.main()




