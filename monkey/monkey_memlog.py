import os
import pytest
import os.path
import time
import glob
import time
import basic_param
def monkey_meminfo():
    devs=basic_param.dev_geted()
    pk = basic_param.pk
    path = basic_param.path
    meminfotime=basic_param.meminfotime
    for dev in devs:

        # for file in glob.glob(os.path.join(path, '*.cmd')):#
      print(dev)
        #   os.remove(file)
      os.system("clear")
      devicedir = os.path.exists(path + dev)
      if devicedir:
            print("file was exist")
      else:
            try:
                os.mkdir(path + dev)
            except Exception as err:
                print(err)
      for i in range(1,meminfotime):
            time.sleep(1)
            os.system(f"adb -s {dev}  shell dumpsys meminfo {pk} :core |grep PSS >>{path}{dev}\meninfo.log\n")
            # os.system("adb shell dumpsys meminfo com.cleanobjects.protectspeedl.boost.android :core |grep PSS >>/Users/yanchenghao/Desktop/log.txt\n")
            time.sleep(2)
            # os.system(f"adb -s {dev} shell date >>{path}{dev}\meninfo.log\n")
            os.system(f"adb -s {dev} shell date >>{path}{dev}\meninfo.log\n")
