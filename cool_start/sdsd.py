import os
import pytest
import os.path
import time
import glob
import time
import basic_param
def start_clear1():
      devs=basic_param.dev_geted()
      pk = basic_param.pk
      path = basic_param.path
      meminfotime=basic_param.meminfotime
    # for dev in devs:

        # for file in glob.glob(os.path.join(path, '*.cmd')):#
      # print(dev)
        #   os.remove(file)
      os.system("cls")
      devicedir = os.path.exists(path + devs[0])
      if devicedir:
            print("file was exist")
      else:
            try:
                os.mkdir(path + devs[0])
            except Exception as err:
                print(err)
      for i in range(1,100):
            time.sleep(15)
            os.system(f"adb -s {devs[0]} shell pm clear {pk}\n")
            time.sleep(1)
            os.system(f"adb -s {devs[0]}  shell am start {pk}/com.africa.news.activity.SplashActivity\n")

start_clear1()