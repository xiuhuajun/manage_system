from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, FileField, TextAreaField
from wtforms.validators import EqualTo, DataRequired, Email, Regexp, ValidationError
# from app.models import User
from App.models import User


class RegistForm(FlaskForm):
    user_name = StringField(label="昵称", validators=[DataRequired("用户名")], description="昵称",
                       )

    phone = StringField(label="手机号码",
                        validators=[DataRequired("请输入手机号码"), Regexp("^1[345678]\\d{9}$", message="手机号码格式不正确")],
                        description="手机号码",
                        )

    pwd = PasswordField(label="密码", validators=[DataRequired("请输入密码")], description="密码",
                        )

    cpwd = PasswordField(label="确认密码", validators=[DataRequired("请输入确认密码"), EqualTo("pwd", message="两次密码不一致")],
                         description="确认密码",
                         )

    # submit = SubmitField("注册")

    # name,email,phone都是唯一的，需要验证唯一性
    # def validate_name(self, field):
    #     name = field.data
    #     user = User.query.filter_by(name=name).count()
    #     if user == 1:
    #         raise ValidationError("昵称已经存在")


    # def validate_email(self, field):
    #     email = field.data
    #     user = User.query.filter_by(email=email).count()
    #     if user == 1:
    #         raise ValidationError("邮箱已经存在")

    # def validate_phone(self, field):
    #     phone = field.data
    #     user = User.query.filter_by(phone=phone).count()
    #     if user == 1:
    #         raise ValidationError("手机号码已经存在")

class LoginForm(FlaskForm):
    user_name = StringField(label="昵称", validators=[DataRequired("用户名")], description="昵称",
                       )

    pwd = PasswordField(label="密码", validators=[DataRequired("请输入密码")], description="密码",
                        )

    # def validate_pwd(self, field):
    #         pwd = field.data
    #         user = User.query.filter_by(password_hash=pwd).count()
    #         if user == 1:
    #             raise ValidationError("密码存在")