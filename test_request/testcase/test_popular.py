import pytest
import requests
from common import log_config
from common import http_requests
from common import yaml_conf
from config import conf
import os

request1=http_requests.HttpRequest()
protocol=conf.get_protocol()
host=conf.get_host()
log_level=conf.get_level()
log_exsion=conf.get_extension()
print(__file__)
name=os.path.split(__file__)[-1].split(".")[0]
print(name)
log_path=name+log_exsion
dir=os.path.dirname(os.path.dirname(__file__))
name=os.path.split(__file__)[-1].split(".")[0]
log_path=name+log_exsion
with open(dir+"/logs/" + log_path,"w") as f:
    f.write(" ")
logger1= log_config.Logger(dir+"/logs/" + log_path, "test", log_level)
header = yaml_conf.yaml_load(dir+"/data/header.yaml")
print("11111111")
# @pytest.fixture()
# def login():
#     path="/api/user/snackUser/login"
#     url1=protocol+host+path
#     data=yaml_conf.yaml_load(dir+"/data/login.yaml")
#     print(data)
#     params=data[0]["data"]#取正确的用例让其执行成功
#     print("444444444")
#     print(params)
#     print(params)
#     logger1.logger.info("当前url:" + url1)
#     logger1.logger.info("当前的测试参数"+str(params))
#     # print(pams)
#     r1=request1.request(url1,headers=header,json=params,http_method="post",timeout=5,verify=False)
#     print(r1)
#     print("333333333")
#     token=r1["body"]["body"]["token"]
#     print(token)
#     return token



path = "/api/content/index/all"
url1=protocol+host+path
print(url1)
# data=yaml_conf.yaml_load(dir+"/data/all.yaml")
# print(data)
# list=[]
# for a in data:
#   list.append(a["data"])
# print(list)
list=yaml_conf.get_yaml_data(dir+"/data/all.yaml")
#[[{'type': 'popular'}, {'code': 1}], [{'type': 'new'}, {'code': 1}]]
print(list)
# print(data[0])
# params=data["type"][0]
# params1=data["type"]
print("1111")
print("sdsdsd")
# print(params1)
#params,check分别对应{'type': 'popular'}，{'code': 1}，
#@pytest.mark.parametrize会把用例列表中多个参数对应
@pytest.mark.parametrize("params,check", list)
# @pytest.mark.usefixtures("login")
# @pytest.mark.usefixtures("login1")
def test_popular(login,params,check):
    # params=params["type"]
    # print(params)
    # params=params["data"]
    print("222222222")
    print(login)
    header["authorization"] = login
    print(params)
    print(url1)
    print(header)
    logger1.logger.info("当前url:" + url1)
    # url="http://api.molelive.com/api/content/index/all"
    logger1.logger.info("当前的测试参数"+str(params))
    logger1.logger.info("当前的check" + str(check))
    # print(pams)
    r1=request1.request(url1,headers=header,params=params,http_method="get",timeout=5,verify=False)
    # r1=requests.get(url1,params=params,headers=header)
    # logger1.logger.info(r1["body"])
    logger1.logger.info("当前的返回结果" + str(r1))
    print(r1)
    assert r1["body"]["code"] == check["code"]
    assert r1["code"] == 200
    # print(r1.content)
    # print(r1.url)
    # print(header)
    # print(r1.request)
    # print(r1.text)
    # assert  r1.status_code==200
    # assert r1.json()["code"] == 1


