from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

def to_goods_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element=driver.find_element_by_link_text("电脑").click()
    # 悬停到电脑上,点击电脑
    # Action=ActionChains(driver)
    # Action.move_to_element(computer_element)
    # Action.click().perform()
    #点击笔记本
    time.sleep(2)
    handles=driver.window_handles
    index_handle=driver.current_url
    print(id(index_handle))
    driver.switch_to.window(handles[-1])
    # for handle in handles:
    #     print(handle)
    #     if handle != index_handle:
    #         print(handle)
    #         driver.switch_to.window(handle)
    driver.find_element_by_link_text("笔记本").click()
    time.sleep(10)
    #点击thinkpad
    #切换语柄
    handles=driver.window_handles
    driver.switch_to.window(handles[-1])
    driver.find_element_by_id("brand-11518").click()
    time.sleep(2)
    #点击评论数
    driver.find_element_by_xpath("//*[@id=\"J_filter\"]/div[1]/div[1]/a[3]/span").click()
    time.sleep(2)
    #点击第一款电脑
    driver.find_element_by_xpath("//*[@id=\"J_goodsList\"]/ul/li[1]/div/div[1]/a/img").click()
    time.sleep(2)
    #切换语柄
    handles=driver.window_handles
    driver.switch_to.window(handles[-1])
    #下拉页面
    js="window.scrollTo(0,1500)"
    driver.execute_script(js)
    #点击规则与包装
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    #解析所有的标签
    time.sleep(2)
    info_elements=driver.find_elements_by_class_name("Ptable-item")
    list_info=[]
    for info_element in info_elements:
        info_element_dict=get_info_element_dict(info_element)
        list_info.append(info_element_dict)
    save_goods_info(list_info)

#保存这些信息到文件中
# driver.find_element_by_xpath("").click()
time.sleep(2)
def get_info_element_dict(info_element):
# 拿到第一列的信息title
    computer_param=info_element.find_element_by_tag_name("h3")
# 拿到key值
    computer_info_keys=info_element.find_elements_by_tag_name("dt")
# 拿到value
    computer_info_values=info_element.find_elements_by_xpath("dl//dd[not(contains(@class,'Ptable-tips'))]")
    key_value_dict={}
    for i in range(len(computer_info_keys)):
        # 假如text方法，将元素改成文本
        key_value_dict[computer_info_keys[i].text]=computer_info_values[i].text
    info_dict={}
    info_dict[computer_param.text]=key_value_dict
    print(info_dict)
    return info_dict

def save_goods_info(list_info):
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"/goods_infos/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file_path+"computer.infos","a",encoding="utf-8") as f:
        f.write(str(list_info))
to_goods_page()