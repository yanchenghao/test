from selenium import webdriver
import sys
from common import screenShot as sc

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
try :
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.jd.com")
    elem=driver.find_element_by_link_text("手机")
    sc.screenshot(driver)
    acton=ActionChains(driver)
    elem.click()
    windows=driver.window_handles
    driver.switch_to.window(windows[1])
    time.sleep(2)
    # phoneCard=driver.find_element_by_tag_name("手机卡")
    # phoneCard.click()
    driver.save_screenshot()
except:
    curent_url=driver.current_url
    driver.get(curent_url)
    phoneCard=driver.find_element_by_tag_name("手机卡")
    phoneCard.click()
    print("sdsds")
    pass
finally:
    time.sleep(3)
    driver.quit()

