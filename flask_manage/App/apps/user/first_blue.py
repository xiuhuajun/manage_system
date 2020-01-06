from flask import Blueprint, render_template, current_app, request, Response, json, jsonify, redirect, make_response, \
    url_for, flash
from App.models import db
from App.models import User
from flask import session

from flask_wtf import csrf
from App.apps.forms import RegistForm,LoginForm

first = Blueprint('first', __name__)

@first.route('/register/',methods=['GET','POST'])
def register():

    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegistForm()
        if form.validate_on_submit():
            data = form.data
            user = User(
                name=data["user_name"],
                password_hash = data["pwd"],
                phone=data["phone"],
                # pwd=generate_password_hash(data["pwd"]),
            )
            # db.session.add(user)
            # db.session.commit()
            user.save()
            flash("注册成功,请登陆！", "ok")
            # return redirect(url_for("home.login"))
            return redirect(url_for('first.login'))
        return render_template("register.html", form=form)

    # form = RegistForm()
    # if request.method == 'GET':

        # csrf_token = csrf.generate_csrf()
        # # print(111)
        # context = {
        #     'csrf_token_s':csrf_token,
        # }
        # res = make_response(render_template('register.html',**context))
        # res.set_cookie("csrf_token",csrf_token)
        # return res
    #     return render_template('register.html',form=form)
    #
    # else:

        # user_name = request.form.get('user_name')
        # phone = request.form.get('phone')
        # pwd = request.form.get('pwd')
        # cpwd = request.form.get('cpwd')
        # allow = request.form.get('allow')  # None 和  on

        # 数据库插入操作
        # try:
            # user = User.objects.create(name=user_name, password=pwd, phone=phone)
            # print('yangle')
            # raise Exception('erroryyy')
            # return HttpResponse('hello')
            # user = User(name=user_name,password_hash=pwd,phone=phone)
            # flag = user.save()
        #     user.save()
        #
        #     # return redirect(url_for('first_blue.login'))
        #     return render_template('login.html')
        # except Exception as e:
        #     print(e)
        #
        # except User.DoesNotExist:
        #     return redirect('/register/')
        # return


@first.route('/user/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # username = request.args.get('username')  # str
        form = LoginForm()
        if form.validate_on_submit():
            data = form.data
            user_name = data.get('user_name')

            # session["username"] = "username"

            pwd = data.get('pwd')
            user = User.query.filter_by(name=user_name,password_hash=pwd).first()
            if user == None:
                print('密码错误')
                context = {
                    'errmsg':'密码错误'
                }

                return render_template('login.html', **context)
            else:
                return '登录成功'


@first.route('/user/code_user/',methods=['GET'])
def code_user():
    if request.method == 'GET':
        username = request.args.get('username') #str
        user = User.query.filter_by(name=username).first()

        flag = False
        # passwd = ''
        if user:
            flag = True
            # for u in user:
            #     passwd = u.password
        # return JsonResponse({'flag': flag, 'passwd': passwd})
        # return Response({'flag':'aa'})
        return jsonify({'flag':flag})

@first.route('/user/code_phone/',methods=['GET'])
def code_phone():
    if request.method == 'GET':
        phone = request.args.get('phone') #str
        user = User.query.filter_by(phone=phone).first()

        flag = False
        if user:
            flag = True
        return jsonify({'flag':flag})






