from selenium import webdriver
import unittest
import time

class TestSignup(unittest.TestCase):
    def test_signup1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.implicitly_wait(5)

        input1 = browser.find_element_by_xpath("//label[contains(text(), 'First name*')]/../input")
        input1.send_keys("sample")
        input2 = browser.find_element_by_xpath("//label[contains(text(), 'Last name*')]/../input")
        input2.send_keys("sample")
        input3 = browser.find_element_by_xpath("//label[contains(text(), 'Email*')]/../input")
        input3.send_keys("sample")

        time.sleep(2)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        self.assertEqual(welcome_text_elt.text, "Congratulations! You have successfully registered!")

        time.sleep(3)
        browser.quit()



    def test_signup2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.implicitly_wait(5)

        input1 = browser.find_element_by_xpath("//label[contains(text(), 'First name*')]/../input")
        input1.send_keys("sample")
        input2 = browser.find_element_by_xpath("//label[contains(text(), 'Last name*')]/../input")
        input2.send_keys("sample")
        input3 = browser.find_element_by_xpath("//label[contains(text(), 'Email*')]/../input")
        input3.send_keys("sample")

        time.sleep(2)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        self.assertEqual(welcome_text_elt.text, "Congratulations! You have successfully registered!")

        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()