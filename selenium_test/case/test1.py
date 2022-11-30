from common import cookiesUnit
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.find_element(*locator)