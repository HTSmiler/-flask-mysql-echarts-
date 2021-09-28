import json
from flask import Blueprint, render_template, jsonify
from app.models import MYSJ,MZSJ,PySJ,SJPL,CSJ
from app.extensions import db
from sqlalchemy import *

main = Blueprint('main', __name__)  # 实例化路由
@main.route('/')
def index():
    rs_gmsj = get_my_sj()
    rs_gpd = get__py_dw()
    rs_gcdw = get_c_dw()
    rs_gscb = get_sj_cbs()
    rs_c =  get_c_dw1()
    return render_template('/main/echarts.html', rs_gmsj=rs_gmsj,rs_gcdw=rs_gcdw,rs_gpd=rs_gpd,rs_gscb=rs_gscb,rs_c=rs_c)
   # return render_template('/main/echarts.html')    # 当url访问 / 直接跳转到主页

#  统计莫言的十本书  获取结果：
def get_my_sj():     # 编写查询语句  返回前10条
    # sql: select * from hot_work group by job_name limit 10
    gmsj_rs = MYSJ.query.order_by(desc('BT')).limit(13)
    print(gmsj_rs)
    return gmsj_rs


# 所有python数据的价格   获取结果
def get__py_dw():
#     # sql: select * from avg_money_city
    gpd_rs = PySJ.query.order_by(desc('JG')).limit(20)
    print('所有python数据的价格     获取结果成功')
    return gpd_rs


def get_c_dw1():
    c_rs_2019 = db.session.query(CSJ.CBSJ, func.count(CSJ.f1).label('c_count'),
                                   func.DATE_FORMAT(CSJ.CBSJ, '%m月').label('month'))\
        .group_by(func.DATE_FORMAT(CSJ.CBSJ,'%Y%m%d'))\
        .having(func.year(CSJ.CBSJ) == 2019).limit(25)

    c_rs_2020 = db.session.query(CSJ.CBSJ, func.count(CSJ.f1).label('c_count'),
                                   func.DATE_FORMAT(CSJ.CBSJ, '%m月').label('month'))\
        .group_by(func.DATE_FORMAT(CSJ.CBSJ,'%Y%m%d'))\
        .having(func.year(CSJ.CBSJ) == 2020).limit(25)
    c_rs = [c_rs_2019, c_rs_2020]
    print('书籍出版时间"：' + str(c_rs))
    return c_rs


# C相关书籍的所有评论数      获取结果
def get_c_dw():
    # sql: select * from avg_money_big_data
    gcdw_rs = CSJ.query.all()
    print('C相关书籍的所有评论数         获取结果成功')
    return gcdw_rs


# 网络书籍的作者
def get_sj_cbs():
    gscb_rs = SJPL.query.all()
    print(" 书籍的作者                获取成功 ")
    return  gscb_rs

