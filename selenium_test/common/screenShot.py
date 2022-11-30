from selenium import webdriver
import os
import time

def screenshot(driver,file_path=None):
    if file_path==None:
        path=os.path.dirname(os.getcwd())
        file_path=path+"/images/"
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        image_name=time.strftime("%Y%m%d-%H%M%S",time.localtime())
        file_path=file_path+image_name+".png"
    driver.save_screenshot(file_path)
