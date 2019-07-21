from flask import Flask,render_template,redirect,url_for,request,session
from exit import db
import config
from models import User
from sqlalchemy import or_

UPLOAD_FOLDER = './file/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/chazhao/')
def chazhao():
    return render_template('chazhao.html')

@app.route('/result/')
def result():
    q = request.args.get('q')
    #全局查询功能
    results = User.query.filter(or_(User.id.contains(q),User.telephone.contains(q),User.username.contains(q),User.content.contains(q)))
    return render_template('result.html',results =results)

@app.route('/register/',methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        content = request.form.get('content')

        user = User(telephone=telephone, username=username, password=password,content=content)
        db.session.add(user)
        db.session.commit()
        return render_template('register.html')

@app.route('/login/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        # return "username:%s  /n  password:%s" % (username, password)
        user = User.query.filter(User.username == username,User.password == password).first()

        session['user_id']=user.id

        if user:
            return render_template('index.html')
        else:
            return "登陆失败！"

@app.route('/change/',methods=["POST","GET"])
def change():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()

        user_username=user.username
    
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        content = request.form.get('content')

        # user.username = username
        # user.telephone = telephone
        # user.password = password
        # user.content = content
        # db.session.commit()


        return render_template('change.html',user_username=user_username)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return "sss"
    elif request.method == 'POST':
        file = request.files['file']
        location = url_for('file', filename="file/1.pdf")
        file.save(location)

if __name__ == '__main__':
    app.run()
