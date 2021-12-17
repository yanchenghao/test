import pytest
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
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
dir=os.path.dirname(os.path.dirname(__file__))
name=os.path.split(__file__)[-1].split(".")[0]
log_path=name+log_exsion
logger1= log_config.Logger(dir+"/logs/" + log_path, "test", log_level)
path="/api/user/snackUser/login"

url1=protocol+host+path
header=yaml_conf.yaml_load("./data/header.yaml")
data=yaml_conf.get_yaml_data("./data/login.yaml")
# data=yaml_conf.yaml_load("./data/login.yaml")
# print("11111111")
# print(data)
# list=[]
# for a in data:
#   list.append(a["data"])
# print(list)
# params=data["pam"]
# print(params)
@pytest.mark.parametrize("pam1", data)
def test_login(pam1):
	# pams=pam1["pam"]
    #  print(pam1)
	logger1.logger.info("当前url:" + url1)
	print(pam1)
	logger1.logger.info("当前的测试参数"+str(pam1))
	# print(pams)
	r1=request1.request(url1,headers=header,json=pam1,http_method="post",timeout=5,verify=False)
	print(r1)
	assert r1["body"]["code"]==1
	assert r1["code"]==200

	# r1 = requests.post(url1, headers=header,json=pams, timeout=5,verify=False)
	# print(r1.status_code)
	# print(r1.json())
	# print(r1.text)
	# print(r1.json()["code"])


