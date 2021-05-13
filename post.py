#!/usr/bin/python3
# -*- coding:UTF-8-*-
# Author: zhuhongqiang
import json
import urllib.request
def post_to_server(post_data):
    post_data['msg_content'] = "测试conteng"
    url = "http://mx20403453.qicp.vip/GROUTH"
    post_data_json = urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    req = urllib.request.Request(method="POST", url=url, data=post_data_json, headers=header_dict)
    r = urllib.request.urlopen(url, post_data_json)
    
    print(r.read())

# if __name__ == "__main__":

post_data={'ID': 'PC', 'dikuai': '222', 'date': '333', 'updata': '444'}
post_to_server(post_data)