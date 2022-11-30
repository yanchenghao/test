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
def login(driver,phone,password):

  el2 = driver.find_element(AppiumBy.XPATH, "//*[@text='Phone']")

  try:
    if el2:
      # print(driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="phone"))
      el2.click()
      time.sleep(3)
      el3=driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/mobile")
      time.sleep(1)
      driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/prefix").click()
      time.sleep(1)
      #选择其他国家
      driver.find_elements(AppiumBy.ID, "com.haflla.soulu:id/code")[3].click()
      time.sleep(1)
      el3.send_keys(phone)
      driver.hide_keyboard()
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
    time.sleep(8)
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

driverConfig=UIapi_config.driver(webdriver)
driver=driverConfig.get_driver()
for i in range(3000001,3000002):
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
  login(driver,i,"Best1234")
  driver.quit()
