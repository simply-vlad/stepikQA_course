from selenium import webdriver

browser = webdriver.Chrome("D:\\PyCharm проекты\\chromedriver.exe")
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element_by_id("submit_button")
button = browser.find_element(By.ID, "submit_button")

