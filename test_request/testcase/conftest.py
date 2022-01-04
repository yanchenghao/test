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
# log_level=conf.get_level()
# log_exsion=conf.get_extension()
# print(__file__)
# name=os.path.split(__file__)[-1].split(".")[0]
# print(name)
# log_path=name+log_exsion
dir=os.path.dirname(os.path.dirname(__file__))
# name=os.path.split(__file__)[-1].split(".")[0]
# log_path=name+log_exsion
# # with open(dir+"/logs/" + log_path,"w") as f:
# #     f.write(" ")
# logger1= log_config.Logger(dir+"/logs/" + log_path, "test", log_level)
header = yaml_conf.yaml_load(dir+"/data/header.yaml")
print("11111111")
#设置前置全局配置
@pytest.fixture(scope="function")
def login():
    path="/api/user/snackUser/login"
    url1=protocol+host+path
    data=yaml_conf.yaml_load(dir+"/data/login.yaml")
    print(data)
    params=data[0]["data"]#取正确的用例让其执行成功
    print("444444444")
    print(params)
    print(params)
    print("登录前置")
    # logger1.logger.info("当前url:" + url1)
    # logger1.logger.info("当前的测试参数"+str(params))
    # print(pams)
    r1=request1.request(url1,headers=header,json=params,http_method="post",timeout=5,verify=False)
    print(r1)
    print("333333333")
    token=r1["body"]["body"]["token"]
    print(token)
    return token


@pytest.fixture(scope="function")
def login1():
    login()
    print("前置")
    yield
    print("后置erefdffdgdfgd")

