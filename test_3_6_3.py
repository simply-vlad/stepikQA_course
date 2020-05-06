import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_time_lesson(browser, link):
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".string-quiz__textarea")
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button")
    button.click()
    hint = browser.find_element_by_css_selector(".smart-hints__hint")
    assert "Correct!" in hint.text
