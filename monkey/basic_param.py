#--coding:utf-8--
import os
import pytest
import os.path
import time
import glob
import time
# def test_mytest():
# path = "d:\\monkey_test\\"
path = "/Users/yanchenghao/Documents/monkey_test/"
pk = "com.cleanobjects.protectspeedl.boost.android"
meminfotime=1000#10sYici
# pk="com.transsnet.news.more.ngblog"
def dev_geted():
    # for file in glob.glob(os.path.join(path, '*.cmd')):
    #   os.remove(file)
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


