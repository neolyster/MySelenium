from selenium import webdriver
import  ProcessData
import numpy as np
import time
class AutoClass():
    driver = webdriver.Chrome()
    url = ""
    IsFirst = True
    SavePath = "."
    def __init__(self):
        self.IsFirst = False
        self.url = ""
        self.driver.get("http://www.icbc.com.cn/icbc/")
    def ChangeSavePath(self,path):
        self.SavePath = path
    def Prepare(self):
        print(self.IsFirst)
        if self.IsFirst == True:
            #print("here1")
            self.driver.get("http://www.icbc.com.cn/icbc/")
            self.IsFirst = False


        elif self.IsFirst == False:
            print("here2")
            time.sleep(5)
            now_handle = self.driver.current_window_handle
            all_handles = self.driver.window_handles
            print(all_handles)
            self.driver.switch_to_window(all_handles[-1])#切换句柄
            print(self.driver.current_url)
            #self.SavePic()
            # for handle in all_handles:
            #     if handle != now_handle:
            #         self.driver.switch_to(handle)
            #         print(self.driver.title)

    def SavePic(self,*args):#保存截图操作
        if len(args)==0:
            Path = self.SavePath + "/test.png"
            #print(Path)
            pic_url = self.driver.get_screenshot_as_file(Path)
            #print(pic_url)
        elif len(args) ==1 :
            str = args[0]
            Path = self.SavePath +"/" + str+".png"
            pic_url = self.driver.get_screenshot_as_file(Path)

    def FindTag(self,list):
        for i in range(10):
            element1 = self.driver.find_element_by_xpath("//*[@id='sMin_amount_input']")
            element1.send_keys(list[i])
            element2 = self.driver.find_element_by_xpath("//*[@id='sMax_amount_input']")
            element2.send_keys(list[i])
            element_spr = self.driver.find_element_by_xpath("//*[@id='spr_col_btn'] ")
            element_spr.click()
            element_sub = self.driver.find_element_by_xpath("//*[@id='submitBtn']")
            element_sub.click()

            element_pic = self.driver.find_element_by_xpath("//*[@id='balanceTaxInfoBody']/tr/td[4]/a")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element_pic)
            Path = self.SavePath + "/" + str(i) + ".png"
            pic_url = self.driver.get_screenshot_as_file(Path)
            time.sleep(2)



