from flask import Flask
from flask import render_template
from flask import request

from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'vanke_zb'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    cursor = mysql.get_db().cursor()
    effect = cursor.execute("insert into `biao` (store,month,day,t1,t2,t3,t4,t5,t6,t7,t8,t9) values('1','1','1','1','1','1','1','1','1','1','1','1')")
    cursor.close()
    return 'a'
    data   = cursor.fetchall()
    print(data)
    biao = ['今天录入房源', '月累计录入房源', '今日跟进房源', '今日录入客源', '月累计录入客源', '今日跟进客源', '今日实堪', '今日新增钥匙', '月累计新增钥匙', '今日网络端口新增', '今日买卖带看', '买卖还价', '月累计买卖带看', '今日租赁带看', '租赁还价', '月累计租赁带看', '今日经理陪看（个）', '今日在谈买卖单', '今日在谈租赁单', '预计明日成交买卖单', '预计明日成交租赁单', '今日一手主推项目', 'call客（个）', '今日派单', '今日一手意向客', '今日成交一手（套）', '明日到访一手意向客', '经理回访一手意向客', '预计明日成交一手（套）', '今日成交租赁（单）', '今日租单合同佣金', '今日租单实收佣金', '今日成交买卖（单）', '今日买卖合佣金', '今日买卖单实收佣金', '今日签独家房源', '今日成交独家房源', '本月累计买卖单', '本月累计租赁单', '本月累计签独家房', '本月累计成交独家房源', '本月签约总业绩（元）', '本月实收业绩（元）']
    print(len(biao))

    return render_template('index.html', biao=biao)

@app.route('/save', methods = ['POST'])
def save():
    cursor = mysql.get_db().cursor()
    effect = cursor.execute('insert into biao values()')
#    date  = request.form['date']
#    store = request.form['store']
#    data  = request.form['data']
    #help(request.form.items())
    print(request.form.getlist('t'))
    print(request.values)
    print(request.form['day'])
    return 'working'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
