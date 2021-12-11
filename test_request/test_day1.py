# import pytest
import datetime
# def test_day11():
#     print("11sdsdfsddfs")
# class Testday1:
#     def test_xing(self):
#         print("1sdfsdfsdfdfe")
now_time = datetime.datetime.now()
now_time.replace("-","")
now_time.replace(" ",".")
now_time.replace(":","")
print(now_time)
