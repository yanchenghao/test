# -*- encoding=utf8 -*-
__author__ = "yanchenghao"
import requests
from airtest.core.api import *
from airtest.core.android.recorder import *
from airtest.core.android.android import *
from airtest.core.android.adb import *
from airtest.report.report import simple_report
def test_zhifu():
    auto_setup(__file__,devices=["Android:///"],compress=90,logdir=True)
    android=Android()
    android.stop_app("com.haflla.soulu")
    android.start_app("com.haflla.soulu")
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    sleep(3.0)
    if  exists(Template(r"tpl1680861128667.png", record_pos=(0.379, -0.596), resolution=(720, 1440))):
            touch(Template(r"tpl1680861160307.png", record_pos=(0.379, -0.594), resolution=(720, 1440)))
    sleep(1)
    if  exists(Template(r"tpl1680861206672.png", record_pos=(0.396, -0.725), resolution=(720, 1440))):

             touch(Template(r"tpl1680861221324.png", record_pos=(0.39, -0.729), resolution=(720, 1440)))

    sleep(1.0)

    touch(Template(r"tpl1681723735677.png", record_pos=(0.374, 0.782), resolution=(720, 1440)))

    sleep(1.0)
    touch(Template(r"tpl1681722111417.png", record_pos=(0.003, -0.081), resolution=(720, 1440)))
    sleep(1.0)
    headers = {
        'country': 'SA',
        'language': 'en',
        'mcc': '-1',
        'appVersionName': '1.1.0',
        'appVersionCode': '35',
        'apiLevel': '10',
        'packageName': 'com.haflla.soulu',
        'packageChannel': 'googleplay',
        'curPackageChannel': 'googleplay',
        'appPlatform': '1',
        'Authorization': 'UwXk++aTCJBiCNvQTVxVy/GTKIC9Y4H4sMhKoPgVrQaubPJxtGs5dDP4Ze178yW5',
        'gender': '1',
        'deviceId': 'e3055c86-733a-4f17-9435-24a59d6179cd',
        'androidId': 'e393549dbbf1d2f4',
        'brand': 'TECNO',
        'model': 'TECNO IN6',
        'sdkInt': '27',
        'netType': 'WIFI',
        'Content-Type': 'application/json',
        'systemCountry': 'CN',
        'systemLanguage': 'zh',
        'Host': 'test-api.souluapp.com',
        'User-Agent': 'okhttp/3.14.9',
    }

    response = requests.get('http://test-api.souluapp.com/api/user/userAccount/getAccountInfo', headers=headers)
    # print(response.json())
    # print(response.json()['body']['coinsBalance'])
    # print(type(response.json()['body']['coinsBalance']))
    a=response.json()['body']['coinsBalance']
    print(a)
    b=a+200
    print(b)
    touch(Template(r"tpl1681722123769.png", record_pos=(0.296, -0.272), resolution=(720, 1440)))
    sleep(1.0)
    touch(Template(r"tpl1681724141033.png", record_pos=(0.004, 0.768), resolution=(720, 1440)))


    sleep(5.0)
    response1 = requests.get('http://test-api.souluapp.com/api/user/userAccount/getAccountInfo', headers=headers)
    # print(response1.json())
    # print(response1.json()['body']['coinsBalance'])
    # print(type(response1.json()['body']['coinsBalance']))
    c=response1.json()['body']['coinsBalance']
    print(c)
    assert(c==b)
    # assert_equal(f"{c}", f"{b}", f"{b}{c}支付是否成功.")
    # simple_report(__file__,logpath=True,output=r"/Users/yanchenghao/airtest/支付.html")



