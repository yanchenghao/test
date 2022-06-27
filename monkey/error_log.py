import os
import pytest
import os.path
import time
import glob
import time
import basic_param
def monkey_errlog():
    from subprocess import Popen
    devs=basic_param.dev_geted()
    pk = basic_param.pk
    path = basic_param.path
    for file in glob.glob(os.path.join(path, '*.cmd')):
            os.remove(file)
    for dev in devs:
        # for file in glob.glob(os.path.join(path, '*.cmd')):#

      print(f"{dev}")
        #   os.remove(file)
      os.system("cls")
      devicedir = os.path.exists(path + dev)
      if devicedir:
            print("file was exist")
      else:
            try:
                os.mkdir(path + dev)
            except Exception as err:
                print(err)
      # os.system(f"adb -s {dev} logcat -b main -v time|findstr E/>{path}{dev}\ppstore1_logcat.logs")
      time.sleep(1)
      # with open(path + dev + "-monkey" + ".bat", "w") as monkey1_file:  #
      #       monkey1_file.write(f"adb -s {dev} shell  monkey -p {pk} -v -v-v  -s 100  --throttle 100  \
      #           --pct-touch 20 --pct-motion 5 --pct-trackball 20 --pct-nav 2 --pct-majornav 19 --pct-syskeys 0 \
      #            --pct-appswitch 32 --pct-anyevent 1  --ignore-security-exceptions  --ignore-crashes --ignore-timeouts \
      #            100000000 1>{path}{dev}\monkey.logs  2>{path}{dev}\error.logs" + "\n")
      # time.sleep(1)
      with open(path + dev + "-logcat" + ".bat", "w") as monkey2_file:
          monkey2_file.write(f"adb -s {dev} logcat -b main -v time|findstr E/>{path}{dev}\ppstore_logcat.log" + "\n")
          monkey2_file.write("pause\n")
          time.sleep(1)
    #   with open(path+dev + "-meninfo" + ".bat", "w") as monkey3_file:#
    #      monkey3_file.write(f"adb -s {dev}  shell dumpsys meminfo {pk}:core |findstr TOTAL: >>{path}{dev}\meninfo.logs\n")
    #      time.sleep(1)
    #      monkey3_file.write(f"adb -s {dev} shell date >>{path}{dev}\meninfo.logs\n")
    #      time.sleep(1)
    #      monkey3_file.write("exit\n")
    #
    for file in os.listdir(path):
     if os.path.isfile(os.path.join(path, file)) == True:
          if file.find('.bat') > 0:
                os.system('start ' + os.path.join(path,file))
                time.sleep(1)
    #       if file.find('meninfo.bat') > 0:
    #           for i in range(1,4):
    #             time.sleep(5)
    #             os.system('start ' + os.path.join(path, file))




