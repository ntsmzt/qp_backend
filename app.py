import flask
import pandas
import csv
import time
import pandas as pd
# excel 处理的库
import xlrd
import xlwt
from xlutils.copy import copy
import os

import json

from requests import *

import pymysql
from flask import Flask, render_template, request, url_for,make_response
#from flask_mysqldb import MySQL
from werkzeug.utils import redirect


app = Flask(__name__)

def sqlshow(res):
    for i in res:
        print(i)

def cont_sql(input_ip='39.103.183.155', input_port=3306, input_user='root', input_passwd='xx3721xx', inpout_databasename='ntsmzt'):
    # 链接服务端
    try:
        dataBase = pymysql.connect(
            host=input_ip,  # MySQL服务端的IP地址
            port=input_port,  # MySQL默认PORT地址(端口号)
            user=input_user,  # 用户名
            password=input_passwd,  # 密码,也可以简写为passwd
            database=inpout_databasename,  # 库名称,也可以简写为db
            charset='utf8',  # 字符编码
            autocommit = True
        )
        cursor = dataBase.cursor()
        print('sucessfully connected!')
        print(type(cursor))
    except Exception as err:
        print(err)
        print(err)
        print('error!')

    # 貌似没有什么显示
    cursor.execute("USE event_zt;")
    print('cursor.execute("USE ntsmzt;")')
    sqlshow(cursor)
    cursor.execute("SHOW TABLES;")
    print('cursor.execute("SHOW TABLES;")')
    sqlshow(cursor)

# login session
@app.route('/login', methods=['POST'])
def get_login_info():
    if request.method == 'POST':
        print(request.json)

    # 序列化成json字符串
    d = {'message': 'check is ok',
         'cookies': '123',
         'token': 'abc'
         }
    j = json.dumps(d)
    resp = make_response(j)
    resp.status = '200'

    # 反序列化成字典
    print(json.loads(j))

    return resp




if __name__ == '__main__':
    app.run(debug=1)
    #cont_sql()





