import requests
import pytest
from common import yaml_conf
from common import http_requests
from common import yaml_conf
from config import conf
import os
import sys
from logs import log_config
request1=http_requests.HttpRequest()
protocol=conf.get_protocol()
host=conf.get_host()
log_level=conf.get_level()
log_exsion=conf.get_extension()
log_path=conf.get_logpath()
logger1=log_config.Logger("logs/login.log","test",log_level)
path="/api/user/snackUser/login"

url1=protocol+host+path
logger1.logger.info(url1)
header=yaml_conf.yaml_load("./data/header.yaml")
@pytest.mark.parametrize("pam1", yaml_conf.yaml_load("./data/login.yaml"))
# pam1=yaml_loader.yaml_get()
def test_login(pam1):
	pams=pam1["pam"]
	# print(pams)
	r1=request1.request(url1,headers=header,json=pams,http_method="post",timeout=5,verify=False)
	assert r1["body"]["code"]==pam1["code"]
	assert r1["code"]==200

	# r1 = requests.post(url1, headers=header,json=pams, timeout=5,verify=False)
	# print(r1.status_code)
	# print(r1.json())
	# print(r1.text)
	# print(r1.json()["code"])


