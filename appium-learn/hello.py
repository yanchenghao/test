import traceback
from appium import webdriver
import time

from selenium.webdriver.common.by import By

server='http://0.0.0.0:4723/wd/hub'
desired_caps={
  "platformName": "Android",
  "platformVersion": "13",
  "deviceName": "emulator-5554",
  "appPackage": "com.mole.talktalk",
  # "appActivity": "com.transsnet.login.act.LoginActivity"
  "appActivity": "com.transsnet.audiolive.act.SplashActivity"
}
driver = webdriver.Remote(server,desired_caps)
try:
  time.sleep(3)
  if driver.find_element(By.ID,"com.mole.talktalk:id/tv_skip"):
    print(driver.find_element(By.ID,"com.mole.talktalk:id/tv_skip").text)
    driver.find_element(By.ID, "com.mole.talktalk:id/tv_skip").click()
    time.sleep(2)
    print("sdfdsd")
    driver.find_element(By.ID,"com.mole.talktalk:id/phone").click()
    print("234234")
    time.sleep(2)
    driver.find_element(By.ID,"com.mole.talktalk:id/prefix").click()
    time.sleep(2)
    a=driver.find_elements(By.ID,"com.mole.talktalk:id/name")
    print((a[0].text))
    a[0].click()
    time.sleep(1)
    driver.find_element(By.ID, "com.mole.talktalk:id/mobile").send_keys("20001")
    # driver.find_element(By.ANDROID_UIAUTOMATOR, "android.widget.EditText").send_keys("30000")

    time.sleep(5)

    c=driver.find_element_by_android_uiautomator('new UiSelector().text("Log In / Sign up")')
    print(c)
    c.click()
    driver.find_element(By.ID, "com.mole.talktalk:id/password").send_keys("Best1234")
    time.sleep(1)
    driver.hide_keyboard()
    driver.find_element(By.ID, "com.mole.talktalk:id/btn_next").click()
  else:
    print("sdsfsdfs")

except:
  print(traceback.format_exc())
finally:
  time.sleep(100)
  driver.quit()
