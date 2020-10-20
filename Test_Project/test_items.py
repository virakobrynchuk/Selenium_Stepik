import time


def test_page_contains_basket(browser):
    time.sleep(12)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), 'No button'

