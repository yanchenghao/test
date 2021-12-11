import yaml
from common import yaml_conf
a=yaml_conf.yaml_load("./config/conf.yaml")

def host_get():
    host=a["base"]["host"][0]
    print(host)
    return host
def protocol_get():
    protocol=a["base"]["protocol"][0]
    print(protocol)
    return protocol


