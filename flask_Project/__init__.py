from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_Project.route.admin.banners import banner_bp
from flask_Project.route.admin.custom import custom_bp
from flask_Project.route.web.index import index_bp
from flask_Project.route.admin.login import login_bp
app = Flask(__name__,static_url_path='/')
# 数据库注册
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
# session的设置
# 密钥
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
# 存活时间
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

# 各板块功能注册到应用程序中
app.register_blueprint(banner_bp)
app.register_blueprint(custom_bp)
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)

@app.route('/')
def qiantai():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
