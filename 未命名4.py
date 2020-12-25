# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:43:24 2020

@author: ZYC
"""

# 从 selenium 中导入 webdriver（驱动）
from selenium import webdriver
import time
# 选择 Chrome 浏览器并打开
browser = webdriver.Chrome()
browser.get('https://wpblog.x0y1.com')
time.sleep(2)
p = browser.find_element_by_tag_name('p')
h1 = browser.find_element_by_class_name('site-title')
article = browser.find_element_by_id('post-34')
a_tags = browser.find_elements_by_tag_name('a')
for tag in a_tags:
    print(tag.text)
    print(tag.get_attribute('href'))
#print(p.text, h1.text, article.text)
browser.quit()