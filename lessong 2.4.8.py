from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium ждать цену
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element_by_css_selector("#book")
button.click()

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

button = browser.find_element_by_css_selector("#solve")
button.click()
