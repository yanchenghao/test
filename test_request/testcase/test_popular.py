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
logger1= log_config.Logger(dir+"/logs/" + log_path, "test", log_level)
header = yaml_conf.yaml_load(dir+"/data/header.yaml")
print("11111111")
@pytest.fixture()
def login():
    path="/api/user/snackUser/login"
    url1=protocol+host+path
    data=yaml_conf.yaml_load(dir+"/data/login.yaml")
    paramlist=data["pam"]
    params=paramlist[0]
    print("444444444")
    print(params)
    print(params)
    logger1.logger.info("当前url:" + url1)
    logger1.logger.info("当前的测试参数"+str(params))
    # print(pams)
    r1=request1.request(url1,headers=header,json=params,http_method="post",timeout=5,verify=False)
    print(r1)
    print("333333333")
    token=r1["body"]["body"]["token"]
    print(token)
    return token



path = "/api/content/index/all"
url1=protocol+host+path
print(url1)
data=yaml_conf.yaml_load(dir+"/data/all.yaml")
params=data["type"][0]
print("sdsdsd")


# @pytest.mark.parametrize("pam1", params)
def test_popular(login):
    print("222222222")
    print(login)
    header["authorization"] = login
    header1 = {
        "country": "CN",
        "language": "en",
        "appVersionName": "1.0.1",
        "appVersionCode": "7",
        "packageName": "com.mole.talktalk",
        "packageChannel": "google",
        "curPackageChannel": "google",
        "appPlatform": "1",
        "Authorization": "7NPZMsDsnIIMBI7shC0AYeeBzPjPvB8PbKdEE+j+H0iubPJxtGs5dDP4Ze178yW5",
        # "Authorization": "h8pIYs+niv4dLK3By6vIFXgpXsEH6uIr1Y9lbhRAveWubPJxtGs5dDP4Ze178yW5",
        "deviceId": "8c154773-5b9a-4b25-bfd9-bf488b7643b9",
        # "deviceId": "1e985fc9-08d7-494f-89f8-1824f581946b",
        "brand": "TECNO",
        "model": "TECNO CG8",
        "sdkInt": "30",
        # "netQuality": "netType: WIFI",
        "Content-Type": "application/json",
        "Host": "apitest.molelive.com",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
        "Connection": "keep-alive"}

    print(params)
    print(url1)
    print(header)
    print(header1)
    logger1.logger.info("当前url:" + url1)
    # url="http://api.molelive.com/api/content/index/all"
    logger1.logger.info("当前的测试参数"+str(params))
    # print(pams)
    #r1=request1.request(url1,headers=header,param=params,http_method="get",timeout=5,verify=False)
    r1=requests.get(url1,params=params,headers=header)
    # assert r1["body"]["code"] == data["code"]
    # assert r1["code"] == 200
    print(r1.content)
    print(r1.url)
    print(header)
    print(r1.request)
    print(r1.text)
    assert  r1.status_code==200


