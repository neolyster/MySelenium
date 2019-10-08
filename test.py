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
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    print(driver.current_url)
    element = driver.find_element_by_name("tj_trnews")
    element = driver.find_element_by_xpath("//div[@name='tj_trnews']")
    element.click()
    driver.back()
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

def func(*args):
    if(len(args) ==0):
        print('0 parameter')
if __name__ == "__main__":
    func()
    webfunc()
    os.system("pause")