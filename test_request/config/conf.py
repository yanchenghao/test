import yaml
from common import yaml_conf
import os
print("获取配置文件")
basedir = os.path.dirname(__file__)
print("basedir:" + basedir)
# a=yaml_conf.yaml_load("C:/Users/tn_chenghao.yan/PycharmProjects/pythonProject/test_request/config/conf.yaml")
# a=yaml_conf.yaml_load("./config/conf.yaml")
a=yaml_conf.yaml_load(basedir+os.sep+"conf.yaml")
print(a)
def get_host():
    host=a["base"]["host"]
    print(host)
    return host
def get_protocol():
    protocol=a["base"]["protocol"]
    print(protocol)
    return protocol
def get_level():
    log_level=a["base"]["log_level"]
    print(log_level)
    return log_level
def get_extension():
    log_extension=a["base"]["log_extension"]
    print(log_extension)
    return log_extension
# def get_logpath():
#     # print(os.path.split(__file__)[-1].split(".")[0])
#     name=os.path.split(__file__)[-1].split(".")[0]+get_extension()
#     dirandname="logs/"+name
#     # print(os.path.split(__file__)[-1].split(".")[0]+get_extension())
#     return dirandname



