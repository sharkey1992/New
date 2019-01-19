from redis import StrictRedis

class Config(object):
    """设置配置类"""
    # 数据库地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/test"
    # 开启数据库修改跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置redis数据库ip端口
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 设置加密字符串
    SECRET_KEY = 'EREREDFS'
    # 设置session存储数据库类型
    SESSION_TYPE = 'redis'
    # 设置数据库配置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db = 1)
    # 对sessionID进行加密处理
    SESSION_USE_SIGNER = True
    # 对session不需要永久储存
    SESSION_PERMANENT = False
    # 进行过期时长设置
    PERMANENT_SESSION_LIFETIME = 86400


class Developmentconfig(Config):
    """线下开发模式配置类"""
    DEBUG = True


class Productionconfig(Config):
    """线上模式配置类"""
    DEBUG = False


config_dict = {
    'development':Developmentconfig,
    'production':Productionconfig
}