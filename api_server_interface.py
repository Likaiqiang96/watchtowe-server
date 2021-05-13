#!/usr/bin/python3
# encoding:utf-8
from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
from gevent import pywsgi
import time
#-----------------------
#import decode_info as di

#-----------------------


#初始化app、api
app = Flask(__name__)
api = Api(app)

GROUTH = [
    {'ID':'location id'},
    {'dikuai':'dikuai id'}
    #{'pwd': 'password'}
]
'''---------------------------------------------------------------------------------
add_argument('per_page', type=int, location='args') str
add_argument中通过指定参数名、参数类型、参数获取方式来获取参数对象并支持做合法性校验
第一个参数是需要获取的参数的名称
参数type: 参数指的类型， 如果参数中可能包含中文需要使用six.text_type. 或直接不指定type
参数location: 获取参数的方式，可选的有args(url中获取)、json(json类型的)、form(表单方式提交)
参数required:是否必要，默认非必要提供  required=True(必须)
参数help:针对必要的参数，如果请求时没有提供，则会返回help中相应的信息
---------------------------------------------------------------------------------'''
parser = reqparse.RequestParser()
#入参parameter，location='json'表示为入参为json格式
#parser.add_argument('ID',   type=str, required=True, help="need location id")
#parser.add_argument('dikuai',type=str, required=True, help="need location id")
parser.add_argument('ID',default='0',type=str)
parser.add_argument('dikuai',default='0',type=str)
parser.add_argument("date",default='0', type=str )
parser.add_argument("updata",default='0', type=str )
#parser.add_argument("user", type=str )
#parser.add_argument("pwd",  type=str )






# 功能方法部分案例
def show_result_by_id(arg0):
    info =di.get_by_ID(arg0)
    return info
def show_result_by_dikuai(arg0):
    info =di.get_by_dikuai(arg0)
    return info

# 路由类，函数get、post、put、delete等实现http请求方法
# url不带入参  /GROUTH
class c_dictList(Resource):
    #类型get，根据列表GROUTH，处理，返回一个新的列表r_GROUTH
    def post(self):
        args = parser.parse_args()
        print("  rec:",args)

        # 构建新参数
        ID = args['ID']
        dikuai =args['dikuai']
        date=args['date']
        # print("============================",type(date),date)
        
        #user = args['user']
        #pwd = args['pwd']
        #print(ID,user,pwd)
        # 调用方法
        time_str=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) 
        info={'ID':ID,'dikuai':dikuai,'date':date,'time':time_str}
        print("  post-->",info)
        return info ,200

    #类型post，在列表GROUTH后添加一个值，并返回列表值
    #不使用post方法
    def get(self):
        info = {"info":"WatchTower",
                "version":"Beta v0.1",
                "author":"HDU team",
                "update":"2021.03.31",
                "usage":GROUTH}
        return info, 201

#设置资源路由api.add_resource（类名，url路径）
#url，不带入参，如：http://127.0.0.1:5000/GROUTH
api.add_resource(c_dictList, '/GROUTH')


if __name__ == '__main__':
    #不设置ip、端口，默认：http://127.0.0.1:5000/
    #app.run(debug=True)
    #设置ip、端口
    
    app.run(host="192.168.132.151", port=5000,debug=True)
    
    #调试地址
    # http://192.168.132.151:5000/GROUTH
    # http://127.0.0.1:5000/GROUTH
    '''
    长期部署
    '''
    # server = pywsgi.WSGIServer(('192.168.132.151', 5000), app)
    # server.serve_forever()
    # app.run()