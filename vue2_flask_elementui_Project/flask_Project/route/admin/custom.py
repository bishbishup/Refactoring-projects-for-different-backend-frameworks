import sqlalchemy.exc
from flask import Flask, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
import os

from urllib.parse import urlparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000
app.config['UPLOAD_FOLDER']='./static/upload'


db = SQLAlchemy(app)

custom_bp = Blueprint('custom', __name__)

# 用户评价功板块

# 删除用户评价
@custom_bp.route('/admin/custom/delete',methods=['GET', 'POST'])
@cross_origin()
def customs_delete():
    try:
        # 把static/upload目录下的也删了
        id = request.args.get('id')
        data = db.session.execute("""SELECT * FROM custom_evaluation_table WHERE ID = '{}' """.format(id)).fetchall()
        parsed_url = urlparse(data[0][3]).path
        image_url = str(parsed_url)
        static_folder = './'
        result = static_folder + image_url
        os.remove(result)
        # 删除数据库的内容
        db.session.execute("""DELETE FROM custom_evaluation_table WHERE ID = '{}'""".format(id))
        db.session.commit()
        res = {
            "message": "删除成功",
            "status_code": 1,
        }
        return res
    except sqlalchemy.exc.SQLAlchemyError as a:
        print(a)
        res = {
            "message": "数据库异常",
            "status_code": 0,
        }
        return res
    finally:
        db.session.close()

# 展示用户评价
@custom_bp.route('/admin/custom',methods=['GET', 'POST'])
@cross_origin()
def customs_show():
    try:
        datalist = []
        data = db.session.execute("""SELECT * FROM custom_evaluation_table""").fetchall()
        for i in data:
            datalist.append({
                'id': i[0],
                'title': i[1],
                'description': i[2],
                'src': i[3]
            })
        res = {
            "message": "数据读取成功",
            "status_code": 1,
            "datalist": datalist
        }
        return res
    except sqlalchemy.exc.SQLAlchemyError as f:
        print(f)
        res = {
            "message": "数据库异常",
            "status_code": 0,
        }
        return res
    finally:
        db.session.close()


# 添加用户评价
@custom_bp.route('/admin/custom/add',methods=['GET', 'POST'])
@cross_origin()
def customs_add():
    title = request.form.get('title')
    description = request.form.get('description')
    file = request.files['file']
    # 需要全部都一起添加不能单个添加
    if not title or not description or not file:
        res = {
            "status_code": 0,
            "message": "添加失败"
        }
        return res
    else:
        fileName = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        src = "http://127.0.0.1:5000" + "/static/upload/" + fileName
        try:
            db.session.execute(
                """INSERT INTO custom_evaluation_table (title,description,src) VALUES ('{}','{}','{}')""".format(title,
                                                                                                                 description,
                                                                                                                 src))
            db.session.commit()

            res = {
                "status_code": 1,
                "message": "添加成功"
            }
            return res
        except sqlalchemy.exc.SQLAlchemyError as j:
            print(j)
            res = {
                "message": "数据库异常",
                "status_code": 0,
            }
            return res
        finally:
            db.session.close()


# 修改用户评价
@custom_bp.route('/admin/custom/edit',methods=['GET', 'POST'])
@cross_origin()
def customs_edit():

    id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    les = request.form.get('file')
    if les == 'null':
        file = ''
    else:
        file = request.files['file']

    data = db.session.execute("""SELECT * FROM custom_evaluation_table WHERE ID = '{}' """.format(id)).fetchall()
    if title is '':
        title = data[0][1]
    if description is '':
        description = data[0][2]
    if file is '':
        src = data[0][3]
    else:
        fileName = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        src = "http://127.0.0.1:5000" + "/static/upload/" + fileName
        parsed_url = urlparse(data[0][3]).path
        image_url = str(parsed_url)
        static_folder = './'
        result = static_folder + image_url
        os.remove(result)
    try:
            db.session.execute(
                """UPDATE custom_evaluation_table SET title = '{}',description = '{}',src = '{}'WHERE ID = '{}'""".format(
                    title, description, src, id))
            db.session.commit()
            res = {
                "status_code": 1,
                "message": "修改成功"
            }
            return res
    except sqlalchemy.exc.SQLAlchemyError as g:
            print(g)
            res = {
                "message": "数据库异常",
                "status_code": 0,
            }
            return res
    finally:
        db.session.close()
