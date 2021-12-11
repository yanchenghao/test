#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os,time
from common import url_param
import sys,random

global false, null, true
false = False
null = None
true = True
path = "D:\\python_log\\"
randoms1 = random.randint(0, 99)
def ads():
  for j in range(3):#ew
   operid="2" #ng
   country="ng"
   package="com.transsnet.news.more.ngblog"
   authorization="patron:id:accesstoken:4e40cc3796b30d3357953a90124f1fe7wCbSxRK+dYIhN1agGrloTUu5kN4AD7pxThd12gmIMsYXccgmexd+A3jkQ7aOr2LpzRp+fM+hLaWAvtRq1nEV+A=="
   url="https://www.more.buzz/api/contentQuery/indexArticles?channelId=for_you&bizType=&extraMsg=eyJuZXRUeXBlIjoiV0lGSSJ9&isFirstPage=true"

   headers={
   "clientid":"app",
   "model":"Infinix+X660",
   "platform":"android",
   "deviceid":"93f1b261-f3a0-4faa-91bc-4cc69c8ed7"+f"{randoms1}",
   "appversion":"4.3.1",
   "channel":"more",
   "curchannel":"more",
   "apilevel":"15",
   "sdkint":"29",
   "operid":f"{operid}",
   "package":f"{package}",
   "debug":"false",
   "country":f"{country}",
   "nettype":"WIFI",
   "lang":"en",
   "brand":"Infinix",
   "mcc":"0",
   "netquality":"POOR",
   "bandwidth":"116.39824813939865",
   "user-agent":"company/more client/more county/ng lan/en operatorId/2 version/4.3.1 build/480 android/10 manufacturer/INFINIX+MOBILITY+LIMITED model/Infinix+X660 channel/more deviceId/93f1b261-f3a0-4faa-91bc-4cc69c8ed7c5",
   "usertype":"2",
   "authorization":f"{authorization}",
   "accept-encoding":"gzip",
   }
   url1,params1= url_param.params_encode(url)
   print(url)
   print(params1)
   r1 = requests.get(url1,headers=headers,params=params1,timeout=5)
   print(r1.status_code)
   statuscode=r1.status_code
   ab= os.path.basename(sys.argv[0])
   print(ab)
   filename=ab[:-3]
   print(filename)
   if statuscode==200:
       print(r1.json())
       r2=r1.json()
       if r2["bizCode"]==10000:
           # for i in range(len(r2["data"])):
           #    if "ads" in r2["data"][i]:
           #          print(i)
        if r2["data"] == "":
            with open(path + filename + ".log", "a") as file1:
                file1.write(f"第{j}次的广告位结果为空")
        else:
            with open(path + filename + ".log", "a") as file1:
                file1.write(f"第{j}次的广告位结果" + "\n")
                # file1.write(r2["bizCode"])
                for i in range(len(r2["data"])):
                    if "ads" in r2["data"][i]:
                        file1.write(f"{i}" + ",")
                file1.write("\n")
            time.sleep(1)
       else:
           with open(path + filename + ".log", "a",encoding='utf-8') as file2:
                   file2.write(f"{r2}"+"\n")
           time.sleep(1)
   else:
       with open(path + filename + "err.log", "a") as file3:
        file3.write(f"第{j}次的结果" + f"{statuscode}"+"\n")
   time.sleep(1)
ads()