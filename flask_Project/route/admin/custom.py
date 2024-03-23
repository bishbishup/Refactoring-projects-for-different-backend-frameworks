import ntpath
import sqlalchemy.exc
from flask import Flask, request, session, redirect, render_template, make_response,url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

custom_bp = Blueprint('custom', __name__)

# 用户评价
@custom_bp.route('/admin/custom',methods=['GET', 'POST'])
def customs():
    if session.get('admin_id') != 1  and request.path != '/admin/login':
        return redirect(url_for('login.login'))
    else:
        if request.method == 'GET':
            if request.args.get('act') == "del":
                try:
                    id1 = request.args.get('id')
                    data1 = db.session.execute("""SELECT * FROM custom_evaluation_table WHERE ID = '{}'""".format(id1)).fetchall()
                    if len(data1) == 0:
                        res = make_response("数据无法找到", 404)
                        return res
                    else:
                        try:
                            os.remove('static/upload/'+data1[0].src)
                            try:
                                id2 = request.args.get('id')
                                db.session.execute("""DELETE FROM custom_evaluation_table WHERE ID = '{}'""".format(id2))
                                db.session.commit()
                                return redirect('custom')
                            except sqlalchemy.exc.SQLAlchemyError as a:
                                print(a)
                                res = make_response("数据库异常", 500)
                                return res
                        except OSError as b:
                            print(b)
                            res = make_response('文件删除失败',500)
                            return res
                except sqlalchemy.exc.SQLAlchemyError as c:
                    print(c)
                    res = make_response("数据库异常", 500)
                    return res
            elif request.args.get('act') == 'mod':
                try:
                    id3 = request.args.get('id')
                    data3 = db.session.execute("""SELECT * FROM custom_evaluation_table WHERE ID = '{}'""".format(id3)).fetchall()
                    if len(data3) == 0:
                        res = make_response("数据无法找到", 404)
                        return res
                    else:
                        try:
                            data4 = db.session.execute("""SELECT * FROM custom_evaluation_table""").fetchall()
                            return render_template('custom.html',evaluations = data4, mod_data=data3[0])
                        except sqlalchemy.exc.SQLAlchemyError as d:
                            print(d)
                            res = make_response("数据库异常", 500)
                            return res
                except sqlalchemy.exc.SQLAlchemyError as e:
                    print(e)
                    res = make_response("数据库异常", 500)
                    return res
            else:
                try:
                    data5 = db.session.execute("""SELECT * FROM custom_evaluation_table""").fetchall()
                    return render_template('custom.html', evaluations=data5)
                except sqlalchemy.exc.SQLAlchemyError as f:
                    print(f)
                    res = make_response("数据库异常", 500)
                    return res

        # 处理post请求
        elif request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            id6 = request.form.get('mod_id')
            file = request.files['file']

            if file.filename:
                fileName = file.filename
                filename = ntpath.basename(fileName)
                file.save(os.path.join('./static/upload', filename))

            else:
                fileName = None

            if fileName:
                if id6:
                    try:
                        data6 = db.session.execute("""SELECT * FROM custom_evaluation_table WHERE ID = '{}'""".format(id6)).fetchall()
                        if len(data6) == 0:
                            res = make_response("数据无法找到", 404)
                            return res
                        else:
                            try:
                                os.remove('static/upload/' + data6[0].src)
                                try:
                                    db.session.execute("""UPDATE custom_evaluation_table SET title = '{}',description = '{}',src = '{}'WHERE ID = '{}'""".format(title, description, fileName, id6))
                                    db.session.commit()
                                    return redirect('custom')
                                except sqlalchemy.exc.SQLAlchemyError as g:
                                    print(g)
                                    res = make_response("数据库异常", 500)
                                    return res
                            except OSError as h:
                                print(h)
                                res = make_response('文件删除失败', 500)
                                return res
                    except sqlalchemy.exc.SQLAlchemyError as i:
                        print(i)
                        res = make_response("数据库异常", 500)
                        return res
                else:
                    try:
                        db.session.execute(
                            """INSERT INTO custom_evaluation_table (title,description,src) VALUES ('{}','{}','{}')""".format(title, description, fileName))
                        db.session.commit()
                        return redirect('custom')
                    except sqlalchemy.exc.SQLAlchemyError as j:
                        print(j)
                        res = make_response("数据库异常", 500)
                        return res
            else:
                if id6:  
                    try:
                        db.session.execute("""UPDATE custom_evaluation_table SET title = '{}',description = '{}'WHERE ID = '{}'""".format(title, description, id6))
                        db.session.commit()
                        return redirect('custom')
                    except sqlalchemy.exc.SQLAlchemyError as k:
                        print(k)
                        res = make_response("数据库异常", 500)
                        return res
                else:  # 添加数据的操作
                    try:
                        db.session.execute("""INSERT INTO custom_evaluation_table (title,description,src) VALUES ('{}','{}','{}')""".format(title, description, fileName))
                        db.session.commit()
                        return redirect('custom')
                    except sqlalchemy.exc.SQLAlchemyError as j:
                        print(j)
                        res = make_response("数据库异常", 500)
                        return res