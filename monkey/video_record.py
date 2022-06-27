import os
import pytest
import os.path
import time
import glob
import time
import basic_param
import datetime
def video_recorder():
    devs=basic_param.dev_geted()
    pk = basic_param.pk
    path = basic_param.path
    meminfotime=basic_param.meminfotime
    for dev in devs:

        # for file in glob.glob(os.path.join(path, '*.cmd')):#
      print(dev)
        #   os.remove(file)
      os.system("cls")
      devicedir = os.path.exists(path + dev)
      if devicedir:
            print("file was exist")
      else:
            try:
                os.mkdir(path + dev)
                os.mkdir(path + dev+"\\v_record")
            except Exception as err:
                print(err)
      for i in range(1,3):
            now_time = datetime.datetime.now()
            now=str(now_time).replace("-","").replace(" ",".").replace(":","")
            os.system(f"adb -s {dev} shell screenrecord --bit-rate 500000 /sdcard/record.mp4\n")
            os.system(f"adb -s {dev} pull /sdcard/record.mp4 {path}{dev}\\v_record\\{i}_{now}.mp4\n")
