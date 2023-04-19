#--coding:utf-8--
import os
import pytest
import os.path
import time
import glob
import time
import os
import pytest
import os.path
import time
import glob
import time
path = "/Users/yanchenghao/Documents/monkey_test/"
pk = "com.haflla.soulu"
meminfotime=1000#10sYici
def dev_geted():
    os.system("clear")
    rt = os.popen('adb devices').readlines()
    for line in rt:
      line=line.lstrip()
      print(line)
    n=len(rt)-2
    ds = list(range(n))
    for i in range(n):
      nPos = rt[i + 1].index("\t")
      ds[i] = rt[i + 1][:nPos]
    return ds
class monkeyconfig():
    def __init__(self,pk,path,meminfotime):
        self.pk=pk
        self.path=path
        self.meminfotime=meminfotime
    def monkey_runing(self):
        from subprocess import Popen
        devs=dev_geted()
        pk = self.pk
        path=self.path
        for file in glob.glob(os.path.join(path, '*.command')):
                os.remove(file)
        for dev in devs:
            # for file in glob.glob(os.path.join(path, '*.cmd')):#

          print(f"{dev}")
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
          # os.system(f"adb -s {dev} logcat -b main -v time|findstr E/>{path}{dev}\ppstore1_logcat.logs")
          time.sleep(1)
          with open(path + dev + "-monkey" + ".command", "w") as monkey1_file:  #
                monkey1_file.write(f"adb -s {dev} shell  monkey -p {pk} -v -v-v  -s 100  --throttle 100  \
                    --pct-touch 20 --pct-motion 5 --pct-trackball 20 --pct-nav 2 --pct-majornav 19 --pct-syskeys 0 \
                     --pct-appswitch 32 --pct-anyevent 1  --ignore-security-exceptions  --ignore-crashes --ignore-timeouts \
                     100000000 1>{path}{dev}/monkey.log  2>{path}{dev}/error.log" + "\n")
          time.sleep(10)

        #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
        for file in os.listdir(path):
         if os.path.isfile(os.path.join(path, file)) == True:
              if file.find('.command') > 0:
                    os.system('sh ' + os.path.join(path,file))
                    time.sleep(5)

    def monkey_meminfo(self):
        devs = dev_geted()
        pk = self.pk
        path = self.path
        meminfotime = self.meminfotime
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
            for i in range(1, meminfotime):
                time.sleep(1)
                os.system(f"adb -s {dev}  shell dumpsys meminfo {pk} :core |grep PSS >>{path}{dev}\meninfo.log\n")
                # os.system("adb shell dumpsys meminfo com.cleanobjects.protectspeedl.boost.android :core |grep PSS >>/Users/yanchenghao/Desktop/log.txt\n")
                time.sleep(2)
                # os.system(f"adb -s {dev} shell date >>{path}{dev}\meninfo.log\n")
                os.system(f"adb -s {dev} shell date >>{path}{dev}\meninfo.log\n")

if __name__ =="__main__":
    # port = 6379
    # name = 'tribe:hot:ids:20201209102029TRB100001640:en'
    m=monkeyconfig("com.haflla.soulu","/Users/yanchenghao/Documents/monkey_test/",1000)
    m.monkey_meminfo()
    m.monkey_runing()
