import sqlalchemy.exc
from flask import Flask, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

banner_bp = Blueprint('banner', __name__)

# banner板块

# 删除功能
@banner_bp.route('/admin/banners/delete',methods=['GET', 'POST'])
@cross_origin()
def banners_delete():
    try:
      id = request.args.get('id')
      db.session.execute("""DELETE FROM banner_table WHERE ID = '{}'""".format(id))
      db.session.commit()
      res = {
         "message": "删除成功",
          "status_code": 1,
      }
      return res
    except sqlalchemy.exc.SQLAlchemyError as c:
      print(c)
      res = {
         "message": "数据库异常",
         "status_code": 0,
      }
      return res
    finally:
        db.session.close()

# 展示功能
@banner_bp.route('/admin/banners',methods=['GET', 'POST'])
@cross_origin()
def banners_show():
    try:
        datalist = []
        data = db.session.execute("""SELECT * FROM banner_table""").fetchall()
        for i in data:
            datalist.append({
                'id': i[0],
                'title': i[1],
                'description': i[2],
                'href': i[3]
            })
        res = {
            "message": "数据读取成功",
            "status_code": 1,
            "datalist": datalist
        }
        return res
    except sqlalchemy.exc.SQLAlchemyError as d:
        print(d)
        res = {
            "message": "数据库异常",
            "status_code": 0,
        }
        return res
    finally:
        db.session.close()

# 添加功能
@banner_bp.route('/admin/banners/add',methods=['GET', 'POST'])
@cross_origin()
def banners_add():
    title = request.get_json().get('title')
    description = request.get_json().get('description')
    href = request.get_json().get('href')
    # 需要全部都一起添加不能单个添加
    if not title or not description or not href:
        res = {
            "status_code": 0,
            "message": "添加失败"
        }
        return res
    else:
        try:
            db.session.execute(
                """INSERT INTO learn.banner_table (title,description,href) value ('{}','{}','{}')""".format(title,
                                                                                                            description,
                                                                                                            href))
            db.session.commit()
            res = {
                "status_code": 1,
                "message": "添加成功"
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

# 修改功能
@banner_bp.route('/admin/banners/edit',methods=['GET', 'POST'])
@cross_origin()
def banners_edit():
    title = request.get_json().get('title')
    description = request.get_json().get('description')
    href = request.get_json().get('href')
    id = request.get_json().get('id')

    try:
        data = db.session.execute("""SELECT * FROM banner_table WHERE ID = '{}' """.format(id)).fetchall()
        if title is '':
            title = data[0][1]
        if description is '':
            description = data[0][2]
        if href is '':
            href = data[0][3]
        db.session.execute(
            """UPDATE learn.banner_table SET title = '{}',description = '{}',href = '{}'WHERE ID = '{}'""".format(title,
                                                                                                                  description,
                                                                                                                  href,
                                                                                                                  id))
        db.session.commit()
        res = {
            "status_code": 1,
            "message": "修改成功"
        }
        return res
    except sqlalchemy.exc.SQLAlchemyError as e:
        print(e)
        res = {
            "message": "数据库异常",
            "status_code": 0,
        }
        return res
    finally:
        db.session.close()
