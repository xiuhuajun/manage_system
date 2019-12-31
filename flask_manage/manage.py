import os
from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app

env = os.environ.get("FLASK_ENV","develop")
app = create_app(env)

manager = Manager(app=app)
manager.add_command('db',MigrateCommand)


if __name__ == "__main__":
    manager.run()

# python manage.py db init     创建迁移文件
# python manage.py db migrate  创建数据库中版本信息
# python manage.py db upgrade  创建数据库中定义的表

