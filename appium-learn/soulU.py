import traceback
from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


for i in range(88888105,88888107):
  server = 'http://0.0.0.0:4723/wd/hub'
  desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "05271259CG000759",
    "appPackage": "com.haflla.soulu",
    # "appActivity": "com.transsnet.login.act.LoginActivity"
    "appActivity": "com.transsnet.audiolive.act.SplashActivity"
  }
  driver = webdriver.Remote(server,desired_caps)
  time.sleep(4)
  el2 = driver.find_element(AppiumBy.XPATH, "//*[@text='Phone']")

  try:
    if el2:
      # print(driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="phone"))
      el2.click()
      time.sleep(2)
      print("sdfdsd")
      el3=driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/mobile")
      el3.send_keys(f"{i}")
      driver.keyevent(4)
      print("234234")
      time.sleep(2)
      driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/text").click()
      time.sleep(2)
      el4=driver.find_element(AppiumBy.ID,"com.haflla.soulu:id/password")
      el4.send_keys("123456")
      driver.hide_keyboard()
      time.sleep(2)
      el4 = driver.find_element(AppiumBy.ID, "com.haflla.soulu:id/btn_next")
      el4.click()

      time.sleep(5)

    else:
      print("sdsfsdfs")

  except:
    print(traceback.format_exc())
  finally:
    time.sleep(10)
    driver.quit()
