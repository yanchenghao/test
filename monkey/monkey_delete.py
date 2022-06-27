import os
import pytest
import os.path
import time
import glob
import time
import basic_param

devs=basic_param.dev_geted()
pk = basic_param.pk
path = basic_param.path
for dev in devs:

    # for file in glob.glob(os.path.join(path, '*.cmd')):#
  print("dev")
    #   os.remove(file)
  os.system("cls")
  a=os.popen(f"adb -s {dev}  shell ps |findstr monkey\n").readline()
  print(a)

  a= a.split(" ")
  b=[]
  for i in range(len(a)):
      if a[i] == "":
        continue
      else:
        b.append(a[i])
  pid=b[1]
  print(b[1])
  # # nPos = rt.split("  ")
  # # print(nPos[4])
  # # pid=nPos[4]
  # time.sleep(1)
  os.system(f"adb -s {dev} shell kill {pid}")
