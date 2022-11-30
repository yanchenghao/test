from common import cookiesUnit
from selenium import webdriver

# driver=webdriver.Chrome()
# driver.maximize_window()
# cookies1=cookiesUnit.cookies(driver)
# if cookies1.checkCookies(driver):
#         driver.get("https://home.jd.com/")
driver=webdriver.Chrome()
driver.maximize_window()
cookies1=cookiesUnit.cookies(driver)
cookies=cookies1.get_cookies()
driver.get("https://www.jd.com")
driver.delete_all_cookies()
# i=0
for cookie in cookies:
    print(cookie)
    if cookie["domain"]!='.jd.com':
        continue
    # 由于selenium的cookies不支持expiry，所以需要去掉
    if "expiry" in cookie.keys():
        # dict支持pop的删除函数
        cookie.pop("expiry")
    # 添加cookies
    driver.add_cookie(cookie)
# cookie=cookies[4]
# for i in range(len(cookies)):
#     if cookies[i]["domain"]!=".jd.com":
#         print(i)
#     print(cookies[i])
# driver.add_cookie(cookie)
# print(cookie)
a=driver.get_cookies()
print("____________")
print(a)
js = "window.open('https://home.jd.com/')"
driver.execute_script(js)
current_url = driver.current_url
# if current_url !="https://home.jd.com/":
#     print("2222")
#     login.login()
# else:
#     pass
# if cookies1.checkCookies(driver):
#     # driver.get("https://home.jd.com/")
#     # cookies1.save_cookies_to_driver(driver)
#     print("sd")
# else:
#     login.login()