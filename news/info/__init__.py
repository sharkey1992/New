from flask import Flask,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import pymysql
from flask_session import Session
from redis import StrictRedis
from config import config_dict
pymysql.install_as_MySQLdb()

# 定义全局对象
db = SQLAlchemy()

# 设置全局变量
redis_store = None

def create_app(config_name):
    # 创建app对象
    app = Flask(__name__)

    # 设置配置方法
    config_class = config_dict[config_name]

    # 配置信息赋予app上
    app.config.from_object(config_class)

    # 初始化加载，当有app时初始化数据库对象
    db.init_app(app)

    global redis_store
    redis_store = StrictRedis(host= config_class.REDIS_HOST,port=config_class.REDIS_PORT,decode_responses=True)

    CSRFProtect(app)
    # 创建一个session工具类对象
    Session(app)

    # 返回app 供调用
    return app