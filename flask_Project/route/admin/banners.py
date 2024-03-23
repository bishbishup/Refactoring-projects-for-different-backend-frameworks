import sqlalchemy.exc
from flask import Flask, request, session, redirect, render_template, make_response,url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

banner_bp = Blueprint('banner', __name__)

# banner设置功能
@banner_bp.route('/admin/banners',methods=['GET', 'POST'])
def banners():
    if  session.get('admin_id') != 1  and request.path != '/admin/login':
        return redirect(url_for('login.login'))
    else:
        if request.method == 'GET':
            if request.args.get('act')== "mod":
                try:
                    id1 = request.args.get('id')
                    data1 = db.session.execute("""SELECT * FROM banner_table WHERE ID = '{}'""".format(id1)).fetchall()
                    if len(data1) == 0:
                        res = make_response("数据无法找到", 404)
                        return res
                    else:
                        try:
                            data2 = db.session.execute("""SELECT * FROM banner_table""").fetchall()
                            return render_template('banners.html', banners=data2, mod_data=data1[0])
                        except sqlalchemy.exc.SQLAlchemyError as a:
                            print(a)
                            res = make_response("数据库异常", 500)
                            return res
                except sqlalchemy.exc.SQLAlchemyError as b:
                    print(b)
                    res = make_response("数据库异常", 500)
                    return res
            elif request.args.get('act')== "del":
                try:
                    id2 = request.args.get('id')
                    db.session.execute("""DELETE FROM banner_table WHERE ID = '{}'""".format(id2))
                    db.session.commit()
                    return redirect('banners')
                except sqlalchemy.exc.SQLAlchemyError as c:
                    print(c)
                    res = make_response("数据库异常", 500)
                    return res
            else:
                try:
                    data3 = db.session.execute("""SELECT * FROM banner_table""").fetchall()
                    return render_template('banners.html', banners=data3)
                except sqlalchemy.exc.SQLAlchemyError as d:
                    print(d)
                    res = make_response("数据库异常", 500)
                    return res

        # 处理post请求
        elif request.method == "POST":
            title = request.form.get('title')
            description = request.form.get('description')
            href = request.form.get('href')
            id3 = request.form.get('mod_id')
            if not title or not description or not href:
                res = make_response("参数异常", 400)
                return res
            else:
                if id3 :
                    try:
                        db.session.execute("""UPDATE learn.banner_table SET title = '{}',description = '{}',href = '{}'WHERE ID = '{}'""".format(title, description, href, id3))
                        db.session.commit()
                        return redirect('banners')
                    except sqlalchemy.exc.SQLAlchemyError as e:
                        print(e)
                        res = make_response("数据库异常", 500)
                        return res
                else:
                    try:
                        db.session.execute("""INSERT INTO learn.banner_table (title,description,href) value ('{}','{}','{}')""".format(title, description, href))
                        db.session.commit()
                        return redirect('banners')
                    except sqlalchemy.exc.SQLAlchemyError as f:
                        print(f)
                        res = make_response("数据库异常", 500)
                        return res