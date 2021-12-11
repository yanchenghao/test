import yaml
import os
pwd=os.getcwd()
print(pwd)
def yaml_get(yaml_path):
    with open(yaml_path, "r", encoding="utf8") as f:
       sd=yaml.load(f,Loader=yaml.FullLoader)
       print(sd)
       return sd
