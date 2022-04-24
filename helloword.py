# print('hello world')

# content = input('\n 按下enter后退出')
# print(content)

# import pymongo
# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.leipin
# collection = db.java
# result = collection.find({}, {'_id': 0, 'place': 1})
# # print(result)
# str = ''
# for i in result:
#     # print(i['place'])
#     str += (i['place'] + ' ')
# print(str)

# str = 'str\nstr'
# print(str)
# arr = str.split('\n')
# print(type(arr))
# print(arr)

#!/usr/bin/evnpython

#!-*- coding:utf-8-*- 
from selenium import webdriver
import time

driver =webdriver.Chrome()

driver get("http://www.baidu.com")

time.sleep(2)

# ********百度输入框的定位方式*******

#通过id方式定位

driver.find_element_by_id("kw").send_keys("selenium")

#通过name方式定位

driver.find_element_by_name("wd").send_keys("selenium")

#通过tag name方式定位

driver.find_element_by_tag_name("input").send_keys("selenium")

#通过class name 方式定位

driver.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过CSS方式定位

driver.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xphan方式定位

driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

driver.find_element_by_id("su").click()

time.sleep(3)

driver.close()