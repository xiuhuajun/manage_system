from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from App.ext import db


class BaseModel(db.Model):
    """定义这个为抽象模型类"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime,
                            default=datetime.now,
                            onupdate=datetime.now)  # 更新时间

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class User(BaseModel):
    """用户模型"""
    __tablename__ = "tbl_user"
    name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    is_delete = db.Column(db.Boolean, default=False)
    is_activate = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)
    itemplans = db.relationship("ItemPlan", backref="user")  # 用户下的项目计划

    def __str__(self):
        return self.name

    @property
    def password(self):
        raise AttributeError("Error Action: Password can't be access")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ItemType(BaseModel):
    """项目类别模块"""
    __tablename__ = 'tbl_itemtype'
    name = db.Column(db.String(100), unique=True)
    parent = db.Column(db.Integer,
                       db.ForeignKey('tbl_itemtype.id'))  # 父项目类别，自关联
    itemplans = db.relationship("ItemPlan", backref="itemtype")  # 项目类别下的所有项目计划

    def __str__(self):
        return self.name


class Province(BaseModel):
    """省份"""
    __tablename__ = "tbl_province"
    name = db.Column(db.String(20), nullable=False)
    # itemplans = db.relationship("ItemPlan", backref="province")  # 省份下的所有项目

    def __str__(self):
        return self.name


class ItemPlan(BaseModel):
    """项目计划模块"""
    __tablename__ = "tbl_itemplan"
    item_type = db.Column(db.Integer,
                          db.ForeignKey("tbl_itemtype.id"),
                          nullable=False)  # 外键关联项目类别
    applicant = db.Column(db.Integer,
                          db.ForeignKey("tbl_user.id"),
                          nullable=False)  # 申请人外键关联用户ID
    province = db.Column(db.Integer,
                         db.ForeignKey("tbl_province.id"),
                         nullable=False)  # 外键关联省份ID

    plan_name = db.Column(db.String(128), nullable=False)  # 计划名称
    estimate_start_time = db.Column(db.DateTime, nullable=False)  # 预计启动时间
    actual_start_time = db.Column(db.DateTime)  #  实际启动时间
    estimate_end_time = db.Column(db.DateTime, nullable=False)  # 预计结束时间
    actual_end_time = db.Column(db.DateTime)  # 实际结束时间
    general_budget = db.Column(db.Float)  # 总预算
    # status_id = db.Column(db.Integer,db.ForeignKey("status.id"),nullable=False)  # 外键关联状态
    status = db.Column(
        db.Enum(
            "WAIT_CHECK",  # 待审核
            "PASS",  # 审核通过
            "REJECTED",  # 审核未通过
            "CANCELED"  # 审核已取消
        ),
        default="WAIT_CHECK",
        # index	如果设为 True，为这列创建索引，提升查询效率
        index=True)  # 审批状态
    commit = db.Column(db.Boolean, default=False)  # 是否提交
    desc = db.Column(db.Text, default="")  # 工作描述
    review = db.Column(db.Boolean, default=False)  # 是否查看
    check = db.relationship("Check", backref="itemplan")  # 审核下的所有项目

    def __str__(self):
        return self.plan_name


class Check(BaseModel):
    """审核记录"""
    __tablename__ = "tbl_check"
    itemplans = db.Column(db.Integer,
                          db.ForeignKey("tbl_itemplan.id"),
                          nullable=False)  # 外键关联计划
    check_person = db.Column(db.Integer,
                             db.ForeignKey("tbl_user.id"),
                             nullable=False)  # 审核人
    result = db.Column(
        db.Enum(
            "WAIT_CHECK",  # 待审核
            "PASS",  # 同意
            "REJECTED",  # 不同意
            "CANCELED"  # 强制取消
        ),
        default="WAIT_CHECK",
        index=True)  #审核结果
    desc = db.Column(db.Text, default="")  # 审核描述
    commit = db.Column(db.Boolean, default=False) # 是否提交
