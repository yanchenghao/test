import os
from common import yaml_conf
class a:
    def sds(self,sd):
        print(sd)
path=os.getcwd()
path1=os.path.abspath(__file__)
path2=os.path.dirname(path1)
path3=os.path.dirname(path2)
print(path)
print(path1)
print(path2)
print(path3)
print(type(path))
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
yaml_conf.yaml_clear()
yaml_conf.yaml_dump(header)
a=yaml_conf.yaml_load("./common/extract.yaml")
print(a["brand"])


