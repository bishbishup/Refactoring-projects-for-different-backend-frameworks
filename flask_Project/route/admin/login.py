import sqlalchemy.exc
from flask import Flask, request, session, redirect, render_template, make_response,url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
import sys
import os
sys.path.append(os.path.abspath('../../libs/common.py'))
from flask_Project.libs.common import md5,MD5_SUFFIX

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

login_bp = Blueprint('login', __name__)


@login_bp.route('/admin/')
def admin2():
    if  session.get('admin_id') != 1  and request.path != '/admin/login':
        return redirect(url_for('login.login'))
    else:
        return render_template('index.html')


# login登录逻辑处理
@login_bp.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # 判断是否是 GET 请求
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = md5(request.form.get('password')+MD5_SUFFIX)
        try:
            data = db.session.execute("""SELECT * FROM admin_table WHERE username = '{}'""".format(username)).fetchall()
            if len(data) == 0:
                res = make_response("管理员账号不存在",400)
                return res
            else:
                if data[0].password == password:
                    session['admin_id'] = data[0].ID
                    return redirect(url_for('login.admin2'))
                else:
                    res = make_response("密码错误", 404)
                    return res
        except sqlalchemy.exc.SQLAlchemyError as a:
            print(a)
            res = make_response("数据库异常", 500)
            return res

@login_bp.route('/admin/<path:sd>')
def sdf(sd):
    return redirect('/admin/login')
