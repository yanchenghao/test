import requests
import pytest
from common import yaml_conf
from common import http_requests
from common import yaml_conf
from config import conf_read
request1=http_requests.HttpRequest()
protocol=conf_read.protocol_get()
host=conf_read.host_get()
path="/api/user/snackUser/login"
url1=protocol+host+path
header=yaml_conf.yaml_load("./data/header.yaml")
print(url1)
@pytest.mark.parametrize("pam1", yaml_conf.yaml_load("./data/test.yaml"))
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


