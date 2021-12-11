import requests
import pytest
from common import yaml_conf
from common import http_requests
from common import yaml_conf
from config import conf_read
request1=http_requests.HttpRequest()
header={"country": "CN",
"language": "en",
"appversionname": "1.0",
"appversioncode": "2",
"packagename": "com.mole.talktalk",
"packagechannel": "",
"curpackagechannel": "",
"appplatform": "1",
"authorization": "",
"deviceid": "8c154773-5b9a-4b25-bfd9-bf488b7643b9",
"brand": "Infinix",
"model": "Infinix X687",
"sdkint": "29",
"netquality": "",
"nettype": "WIFI",
"content-type": "application/json; charset=UTF-8",
"content-length": "91",
"accept-encoding": "gzip",
"user-agent": "okhttp/3.14.9"}

protocol=conf_read.protocol_get()
host=conf_read.host_get()
# pam={
# 	"countryPhoneCode": "1",
# 	"password": "6d9597d054fab29693d255612e67bd6c",
# 	"phone": "2565555555"
# }
path="/api/user/snackUser/login"
url1=protocol+host+path
print(url1)
@pytest.mark.parametrize("pam1", yaml_conf.yaml_load("./data/test.yaml"))
# pam1=yaml_loader.yaml_get()
def test_login(pam1):
	# pams=pam1[0]
	# print(pam1)
	# print(type(pam1))
	pams=pam1["pam"]
	# print(pams)
	r1=request1.request(url1,headers=header,json=pams,http_method="post",timeout=5,verify=False)
	# r1 = requests.post(url1, headers=header,json=pams, timeout=5,verify=False)
	# print(r1.status_code)
	# print(r1.json())
	# print(r1.text)
	# print(r1.json()["code"])
	assert r1["body"]["code"]==pam1["code"]
	assert r1["code"]==200



