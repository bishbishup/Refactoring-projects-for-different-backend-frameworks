import sqlalchemy.exc
from flask import Flask, request, session,Blueprint
from flask_sqlalchemy import SQLAlchemy
import sys
import os
from flask_cors import cross_origin
sys.path.append(os.path.abspath('../../libs/common.py'))
from flask_Project.libs.common import md5,MD5_SUFFIX

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

login_bp = Blueprint('login', __name__)


# login登录逻辑处理
@login_bp.route('/admin/login', methods=['GET', 'POST'])
@cross_origin()
def login():
    username = request.get_json().get('username')
    password = md5(request.get_json().get('password')+MD5_SUFFIX)
    try:
            data = db.session.execute("""SELECT * FROM admin_table WHERE username = '{}'""".format(username)).fetchall()
            if len(data) == 0:
                res = {
                    "message":"用户不存在",
                    "status_code":0,
                    'token':''
                }
                return res
            else:
                if data[0].password == password:
                    session['admin_id'] = data[0].ID
                    res = {
                        "message": "登录成功",
                        "status_code": 1,
                        'token': password
                    }
                    return res
                else:
                    res = {
                        "message": "密码错误",
                        "status_code": 0,
                        'token': ''
                    }
                    return res
    except sqlalchemy.exc.SQLAlchemyError as a:
            print(a)
            res = {
                "message": "数据库异常",
                "status_code": 0,
                'token': ''
            }
            return res
    finally:
            db.session.close()

