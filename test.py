from selenium import webdriver
import  time
import xlrd
import numpy as np
import os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#网页操作
def webfunc():

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    #driver.maximize_window() bug
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    print(driver.current_url)
    element = driver.find_element_by_name("tj_trnews")
    element = driver.find_element_by_xpath("/html/body/div[@id='wrapper']/div[@id='head']/div[@class='head_wrapper']/div[@id='u1']/a[@class='mnav'][1]")
    element.click()

    # 将滚动条移动到页面的底部
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    js = "window.scrollTo(0,document.body.scrollHeight)"
    for i in range(10):
        time.sleep(1)
        driver.execute_script(js)

    element1 = driver.find_element_by_xpath("/html[@class='expanded']/body/div[@id='body']/div[@class='DiscoveryNews']/div[@id='col-discovery']/div[@class='l-left-col col-mod']/ul[@class='ulist focuslistnews'][1]/li[@class='bold-item']/a")
    driver.execute_script("arguments[0].scrollIntoView(true);", element1)
    #driver.maximize_window()
    driver.execute_script(js)
    driver.execute_script("window.scrollBy(0,-500)")
    #driver.back()
# name = driver.find_element_by_id("KeyWord")
# name.send_keys("data_operation")

# data = xlrd.open_workbook(r'E:\Files\Desktop\组会\data\data.xlsx')
# table = data.sheets()[0]
# nrows = table.nrows#多少行
# ncols = table.ncols#多少列
# print(nrows)
# print(ncols)
#
# x = table.col_values(1)[10]
# print(x)
def Webfunc():
    driver = webdriver.Chrome()

def xlsfunc(filedir):
    list = []
    data = xlrd.open_workbook(filedir)
    table = data.sheets()[0]
    list = table.col_values(4)  # 第五列数据
    list2 = table.col_values(4, 7, 17)  # 先试验10个数据
    print(list2)
    # print(len(list))
    return list2


def func(*args):
    if(len(args) ==0):
        print('0 parameter')
if __name__ == "__main__":
    func()
    webfunc()
    os.system("pause")