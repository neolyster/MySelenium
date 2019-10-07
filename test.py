from selenium import webdriver
import  time
import xlrd
import numpy as np
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#网页操作
driver = webdriver.Chrome()
driver.get("http://www.icbc.com.cn/icbc/")
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
print(driver.current_url)

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