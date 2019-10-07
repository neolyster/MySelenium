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
        self.IsFirst = True
        self.url = ""

    def ChangeSavePath(self,path):
        self.SavePath = path
    def Prepare(self):
        print(self.IsFirst)
        if self.IsFirst == True:
            print("here1")
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
            self.SavePic()
            # for handle in all_handles:
            #     if handle != now_handle:
            #         self.driver.switch_to(handle)
            #         print(self.driver.title)

    def SavePic(self):
        Path = self.SavePath + "/test.png"
        #print(Path)
        pic_url = self.driver.get_screenshot_as_file(Path)
        #print(pic_url)
