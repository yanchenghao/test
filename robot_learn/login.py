import requests
def login1():
    headers={
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://test.management.more.buzz/cms/cms/login?ok_url=https%3A%2F%2Ftest.management.more.buzz%2Fcms%2Ftalk%2F",
    "sec-ch-ua": "Google Chrome",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    body={
    "username": "xiaohan.wang",
    "password": "S123456789",
    }

    url="https://test.management.more.buzz/user/login"

    res = requests.post(url, data=body, timeout=2)
    print(res.text)
    print(res.headers)
    print(res.cookies)
    #将CookieJar转为字典：
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    print(cookies)
    if res.status_code==200:
        return "测试后台登录成功"
    else:
        "登录失败"
