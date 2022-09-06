import traceback
from common import log_config
import pytest
from appium import webdriver
import os
import time
from common import yaml_conf
from config import conf

from selenium.webdriver.common.by import By


server='http://0.0.0.0:4723/wd/hub'
desired_caps={
  "platformName": "Android",
  "platformVersion": "13",
  "deviceName": "emulator-5554",
  "appPackage": "com.transsnet.moreplus",
  "appActivity": "com.africa.news.activity.SplashActivity"
}
driver = webdriver.Remote(server,desired_caps)
try:
  time.sleep(10)

except:
  print(traceback.format_exc())
finally:
  time.sleep(2)
  driver.quit()
