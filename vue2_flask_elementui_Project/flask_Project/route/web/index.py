import sqlalchemy.exc
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{'root'}:{'1234'}@{'127.0.0.1'}:{'3306'}/{'learn'}?charset=utf8"
app.config['SECRET_KEY'] = "skfhfdlfsfkhk"
app.config['PERMANENT_SESSION_LIFETIME'] = 20*60*1000

db = SQLAlchemy(app)

index_bp = Blueprint('index', __name__)

# 前台数据处理
@index_bp.route('/get_custom_evaluations',methods=['GET'])
@cross_origin()
def web2():
    try:
        datalist = []
        data = db.session.execute("""SELECT * FROM custom_evaluation_table """).fetchall()
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
    except sqlalchemy.exc.SQLAlchemyError as a:
        print(a)
        res = {
            "message": "数据库异常",
            "status_code": 0,
        }
        return res
    finally:
        db.session.close()
