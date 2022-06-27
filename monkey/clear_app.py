import os
a=os.popen("adb shell pm list package|findstr more").readlines()
print(a)
for i in a:
    i.strip()
    pk=i[8:]
    print(pk)
    os.system(f"adb shell pm clear {pk}")