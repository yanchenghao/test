
class driver:#获取driver
    def __init__(self,webdriver):
        self.webdriver=webdriver
    def get_driver(self):
        server = 'http://0.0.0.0:4723/wd/hub'
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "05271259CG000759",
            "appPackage": "com.haflla.soulu",
            # "appActivity": "com.transsnet.login.act.LoginActivity"
            "appActivity": "com.transsnet.audiolive.act.SplashActivity"
        }
        driver = self.webdriver.Remote(server, desired_caps)
        return driver
# class press:#按压操作
