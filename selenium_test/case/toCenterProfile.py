import selenium
from selenium import webdriver
from common import cookiesUnit
import login
try:
    driver=webdriver.Chrome()
    driver.maximize_window()
    cookies1=cookiesUnit.cookies(driver)
    #判断cookies是否过期且添加cookies到driver
    if cookies1.checkCookies(driver):
        driver.get("https://home.jd.com/")
    else:
        login.login()

except:
    curent_url=driver.current_url
    print(curent_url)
    pass
finally:
    curent_url=driver.current_url
    print(curent_url)
    pass
