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

from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#添加有关操作数据库的文件
#from app import models,views