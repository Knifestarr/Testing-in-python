from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.bing.com/")
element = driver.find_element( By.NAME,"q")
element.send_keys("Arrays")
time.sleep(3)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.bing.com/")
element = driver.find_element( By.NAME,"q")
element.send_keys("Arrays")
time.sleep(3)