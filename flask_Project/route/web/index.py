import sqlalchemy.exc
from flask import Flask,make_response,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

index_bp = Blueprint('index', __name__)

# 前台数据处理
@index_bp.route('/get_banners',methods=['GET'])
def web1():
    try:
        data = db.session.execute("""SELECT * FROM banner_table """).fetchall()
        steps = []
        for (id,title,description,href) in data:
            step = {"ID":int(id),"title":title,"description":description,"href":href}
            steps.append(step)
        return jsonify(steps)
    except sqlalchemy.exc.SQLAlchemyError as a:
        print(a)
        res = make_response("数据库异常", 500)
        return res

@index_bp.route('/get_custom_evaluations',methods=['GET'])
def web2():
    try:
        data = db.session.execute("""SELECT * FROM custom_evaluation_table """).fetchall()
        steps = []
        for (id, title, description, src) in data:
            step = {"ID": int(id), "title": title, "description": description, "src": src}
            steps.append(step)
        return jsonify(steps)
    except sqlalchemy.exc.SQLAlchemyError as a:
        print(a)
        res = make_response("数据库异常", 500)
        return res
