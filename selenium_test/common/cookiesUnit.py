import os, json

class cookies():

    def __init__(self,driver):
        self.driver=driver
#保存cookies到文件
    def save_cookies(self,driver):
        path = os.path.dirname(os.getcwd())
        file_path = path + "/cookies/"
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        cookies = driver.get_cookies()
        with open(file_path + "jdcookies.json", "w") as co:
            co.truncate()
            json.dump(cookies, co)
#验证cookies是否到期
    def checkCookies(self,driver):
# 将cookies文件保存到driver中
        driver=self.save_cookies_to_driver(driver)
        driver.get("https://home.jd.com/")
        current_url=driver.current_url
#判断登录状态
        login_status=False
        if  current_url=="https://home.jd.com/":
            login_status=True
            return login_status
        else:
            return login_status
    def save_cookies_to_driver(self,driver):
        cookies=self.get_cookies()
        driver.get("https://www.jd.com")
        driver.delete_all_cookies()
        for cookie in cookies:
            print(cookie)
            if cookie["domain"] != '.jd.com':
                continue
            # 由于selenium的cookies不支持expiry，所以需要去掉
            if "expiry" in cookie.keys():
                # dict支持pop的删除函数
                cookie.pop("expiry")
            # 添加cookies
            driver.add_cookie(cookie)

        return driver

    def get_cookies(self):
        file_path=os.path.dirname(os.getcwd())
        file=file_path+"/cookies/"+"jdcookies.json"
        with open(file,"r") as fileopen:
            cookiesjson=fileopen.readline()
            cookies=json.loads(cookiesjson)

        print(cookies)
        return cookies

