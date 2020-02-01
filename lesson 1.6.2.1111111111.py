from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.degreesymbol.net")

link = browser.find_element_by_link_text("» Degree symbol examples")
link.click()

