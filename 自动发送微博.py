# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:15:09 2020

@author: ZYC
"""

import requests

class Weibospider:
    
    def __init__(self, username, password):
        self.session = requests.Session()
        self.headers = {
    'user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Mobile Safari/537.36',
    'referer':'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2'
    }
        self.session.headers.update(self.headers)
        self.username = username
        self.password = password
        
    def login(self): 
        login_data = {
              "username":self.username,
              "password":self.password,
              "savestate":"1",
              "r":"https://m.weibo.cn/",
              "ec":"0",
              "pagerefer":"https://m.weibo.cn/login?backURL=https%3A%2F%2Fm.weibo.cn%2F",
              "entry":"mweibo",
              "wentry":"",
              "loginfrom":"",
              "client_id":"",
              "code":"",
              "qq":"",
              "mainpageflag":"1",
              "hff":"",
              "hfp":""
              }
        self.session.post('https://passport.weibo.cn/sso/login', data=login_data)
        
    def get_st(self):
        config_req = self.session.get('https://m.weibo.cn/api/config')
        config = config_req.json()
        st = config['data']['st']
        return st
    
    def compose(self, content):
        comment_data = {"content":content,"visible":"1","st":self.get_st(),"_spr":"screen:360x640"}
        comment_req = self.session.post('https://m.weibo.cn/api/statuses/update', data=comment_data)
        print(comment_req.json())
        
    def send(self, content):
        self.login()
        self.compose(content)

weibospider = Weibospider('15801013723', 'zyc930805#3')
weibospider.send('20200922-zz')        
    
        