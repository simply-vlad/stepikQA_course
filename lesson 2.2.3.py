from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
b = webdriver.Chrome()
b.get(link)

num1 = b.find_element_by_css_selector("#num1").text
num2 = b.find_element_by_css_selector("#num2").text
sum = str(int(num1) + int(num2))
print(sum)

select = Select(b.find_element_by_css_selector("#dropdown"))
select.select_by_value(sum)
b.find_element_by_css_selector(".btn").click()
