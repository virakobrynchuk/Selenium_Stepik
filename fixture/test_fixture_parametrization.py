import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestOpenPage(object):
    def test_open_page(self, browser, link):
        link = "https://stepik.org/lesson/{}/step/1".format(link)
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.find_element_by_tag_name('textarea').send_keys(str(answer))
        browser.find_element_by_class_name('submit-submission ').click()
        result = browser.find_element_by_class_name('smart-hints__hint').text
        assert result == "Correct!"

