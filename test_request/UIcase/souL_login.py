import sys
import os
import traceback

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from appium import webdriver
os.system("pwd")
sys.path.append("/Users/yanchenghao/PycharmProjects/PycharmProjects/pythonProject/appium-learn/UIcase")

from common import UIapi_config
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
def login(driver,phone,password):
  time.sleep(3)
  el2 = driver.find_element(AppiumBy.XPATH, "//*[@text='Phone']")

  try:
    if el2:
      # print(driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="phone"))
      el2.click()
      time.sleep(3)
      el3=driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/mobile")
      el3.send_keys(phone)
      driver.keyevent(4)
      time.sleep(1)
      driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/text").click()
      time.sleep(5)
      size=driver.get_window_size()
      print(size)
      touchobject=TouchAction(driver)
      touchobject.tap(x=200, y=200).release().perform()
      time.sleep(2)
      el4=driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/password")
      time.sleep(3)
      el4.send_keys(password)
      driver.hide_keyboard()
      time.sleep(2)
      el4 = driver.find_element(AppiumBy.ID, "com.haflla.soulu:id/btn_next")
      el4.click()

    else:
      print("sdsfsdfs")

  except:
    print(traceback.format_exc())
  finally:
    time.sleep(2)
def login_Multiple(driver,phoneStart,phoneEnd,password):
  for i in range(phoneStart,phoneEnd):
    # server = 'http://0.0.0.0:4723/wd/hub'
    # desired_caps = {
    #   "platformName": "Android",
    #   "platformVersion": "10",
    #   "deviceName": "05271259CG000759",
    #   "appPackage": "com.haflla.soulu",
    #   # "appActivity": "com.transsnet.login.act.LoginActivity"
    #   "appActivity": "com.transsnet.audiolive.act.SplashActivity"
    # }
    # driver = webdriver.Remote(server,desired_caps)
    time.sleep(4)
    login(driver,i,password)
    driver.quit()
driverConfig=UIapi_config.driver(webdriver)
driver=driverConfig.get_driver()
login(driver, 3000007, "Best1234")
driver.quit()

