from flask import Flask
from flask import render_template
from flask import request

from flask_pymongo import PyMongo

import time


app = Flask(__name__)
app.name = 'test'
mongo = PyMongo(app)

#biao = ['今天录入房源', '月累计录入房源', '今日跟进房源', '今日录入客源', '月累计录入客源', '今日跟进客源', '今日实堪', '今日新增钥匙', '月累计新增钥匙', '今日网络端口新增', '今日买卖带看', '买卖还价', '月累计买卖带看', '今日租赁带看', '租赁还价', '月累计租赁带看', '今日经理陪看（个）', '今日在谈买卖单', '今日在谈租赁单', '预计明日成交买卖单', '预计明日成交租赁单', '今日一手主推项目', 'call客（个）', '今日派单', '今日一手意向客', '今日成交一手（套）', '明日到访一手意向客', '经理回访一手意向客', '预计明日成交一手（套）', '今日成交租赁（单）', '今日租单合同佣金', '今日租单实收佣金', '今日成交买卖（单）', '今日买卖合佣金', '今日买卖单实收佣金', '今日签独家房源', '今日成交独家房源', '本月累计买卖单', '本月累计租赁单', '本月累计签独家房', '本月累计成交独家房源', '本月签约总业绩（元）', '本月实收业绩（元）']
match = {'month': '月', 'day': '日', 'store_id': '门店', 'create_time': '填写时间', 't5': '今日跟进客源', 't18': '今日在谈租赁单', 't17': '今日在谈买卖单', 't40': '本月累计成交独家房源', 't3': '今日录入客源', 't41': '本月签约总业绩（元）', 't36': '今日成交独家房源', 't7': '今日新增钥匙', 't26': '明日到访一手意向客', 't12': '月累计买卖带看', 't30': '今日租单合同佣金', 't2': '今日跟进房源', 't38': '本月累计租赁单', 't14': '租赁还价', 't9': '今日网络端口新增', 't34': '今日买卖单实收佣金', 't25': '今日成交一手（套）', 't27': '经理回访一手意向客', 't15': '月累计租赁带看', 't33': '今日买卖合佣金', 't22': 'call客（个）', 't24': '今日一手意向客', 't37': '本月累计买卖单', 't39': '本月累计签独家房', 't31': '今日租单实收佣金', 't4': '月累计录入客源', 't32': '今日成交买卖（单）', 't21': '今日一手主推项目', 't29': '今日成交租赁（单）', 't35': '今日签独家房源', 't6': '今日实堪', 't13': '今日租赁带看', 't42': '本月实收业绩（元）', 't20': '预计明日成交租赁单', 't10': '今日买卖带看', 't28': '预计明日成交一手（套）', 't11': '买卖还价', 't0': '今天录入房源', 't23': '今日派单', 't8': '月累计新增钥匙', 't16': '今日经理陪看（个）', 't1': '月累计录入房源', 't19': '预计明日成交买卖单'}
key = ['month', 'day', 'store_id', 't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27', 't28', 't29', 't30', 't31', 't32', 't33', 't34', 't35', 't36', 't37', 't38', 't39', 't40', 't41', 't42', 'create_time']

@app.route('/')
def index():
#    user = mongo.db.zb.find()
#    for i in user:
#        print(i)
#    print(user)
#    mongo.db.zb.insert({'new': 'haha'})

    return render_template('index.html', biao=match)


@app.route('/store', methods = ['POST'])
def store():
    data = {}
    for item in request.form.items():
        if item[1] != '':
            data[str(item[0])] = item[1]
        else:
            data[str(item[0])] = '0'
    data['create_time'] = int(time.time())
    print(data)
    mongo.db.zb.insert(data)

    return '提交成功'


@app.route('/compute/')
def compute():
    items = request.args.items()
    gets  = {}
    for item in items:
        gets[item[0]] = str(item[1])
    today = list(mongo.db.zb.find(gets))

    store = mongo.db.store.find_one()
    for i in range(len(today)):
        name = store[today[i]['store_id']]
        today[i]['store_id'] = name
        create = time.localtime(today[i]['create_time'])
        today[i]['create_time'] = time.strftime("%m-%d %H:%M", create)

    return render_template('compute.html', data=today, biao=match, key=key)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
