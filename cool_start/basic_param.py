#--coding:utf-8--
import os
import pytest
import os.path
import time
import glob
import time
# def test_mytest():
path = "d:\\monkey_test\\"
pk = "com.transsnet.news.more.ngblog"
meminfotime=10#10sYici
# pk="com.transsnet.news.more.ngblog"
def dev_geted():
    # for file in glob.glob(os.path.join(path, '*.cmd')):
    #   os.remove(file)
    os.system("cls")
    rt = os.popen('adb devices').readlines()
    for line in rt:
      line=line.lstrip()
      print(line)
    n=len(rt)-2

    ds = list(range(n))
    for i in range(n):
      path = "d:\\monkey_test\\"
      # list=rt[i+1].split("\t")
      # phonemodel=list[i]
      # dev=phonemodel#
      nPos = rt[i + 1].index("\t")
      ds[i] = rt[i + 1][:nPos]
    return ds


