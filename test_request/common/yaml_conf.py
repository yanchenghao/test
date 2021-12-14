import yaml
import os
from os.path import *
# pwd=os.getcwd()
# print(pwd)
extrayaml = dirname(abspath(__file__)) + sep + "extract.yaml"
#提取yaml文件数据
def yaml_load(yaml_path):
    with open(yaml_path, "r", encoding="utf8") as f:
       sd=yaml.load(f,Loader=yaml.FullLoader)
       print(sd)
       return sd
#将字典，生成yaml文件
def yaml_dump(extract_dict):
    with open(extrayaml,"a") as f:
        sd=yaml.dump(extract_dict,f,encoding="utf-8",allow_unicode=True)
#清除yaml 文件
def yaml_clear():
    with open(extrayaml,"w") as f:
        f.truncate()

