from selenium import webdriver
from selenium.webdriver.common.by import By

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)


x_element = browser.find_element(By.CSS_SELECTOR,'#input_value')
x = x_element.text
y = calc(x)

button=browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

text = browser.find_element(By.CSS_SELECTOR,'#answer')
text.send_keys(y)

check=browser.find_element(By.CSS_SELECTOR,'#robotCheckbox')
check.click()

ratio=browser.find_element(By.CSS_SELECTOR,'#robotsRule')
ratio.click()
button.click()
