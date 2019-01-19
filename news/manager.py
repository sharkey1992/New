from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask import session
from info import create_app,db

# 创建app对象 （配置方法名）
app = create_app('development')

# 创建管理对象
manager = Manager(app)

#创建迁移对象
Migrate(app,db)

# 创建迁移命令
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()