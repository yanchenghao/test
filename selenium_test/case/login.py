from selenium import webdriver
import sys
from common import screenShot as sc
from common import cookiesUnit
import time,json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def login():
    try :

        driver = webdriver.Chrome()
        cookies1 = cookiesUnit.cookies(driver)
        driver.maximize_window()
        driver.get("https://www.jd.com")
        time.sleep(2)
        driver.find_element_by_link_text("你好，请登录").click()
        driver.find_element_by_link_text("账户登录").click()
        time.sleep(1)
        driver.find_element_by_id("loginname").send_keys("18712776993")
        driver.find_element_by_id("nloginpwd").send_keys("best123")
        driver.find_element_by_id("loginsubmit").click()
        cookies=driver.get_cookies()
        cookies1.save_cookies(driver)
        # phoneCard=driver.find_element_by_tag_name("手机卡")
        # phoneCard.click()
        # driver.save_screenshot()
    except:
        curent_url=driver.current_url
        print(curent_url)
        pass
    finally:
         time.sleep(3)
         driver.quit()
