from flask import Flask
from flask import render_template
from flask import request

import re

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    biao = ['今日录入房源', '月累计录入房源', '今日跟进房源', '今日录入客源', '月累计录入客源', '今日跟进客源', '今日实堪', '今日新增钥匙', '月累计新增钥匙', '今日网络端口新增', '今日买卖带看', '买卖还价', '月累计买卖带看', '今日租赁带看', '租赁还价', '月累计租赁带看', '今日经理陪看（个）', '今日在谈买卖单', '今日在谈租赁单', '预计明日成交买卖单', '预计明日成交租赁单', '今日一手主推项目', 'call客（个）', '今日派单', '今日一手意向客', '今日成交一手（套）', '明日到访一手意向客', '经理回访一手意向客', '预计明日成交一手（套）', '今日成交租赁（单）', '今日租单合同佣金', '今日租单实收佣金', '今日成交买卖（单）', '今日买卖合佣金', '今日买卖单实收佣金', '今日签独家房源', '今日成交独家房源', '本月累计买卖单', '本月累计租赁单', '本月累计签独家房', '本月累计成交独家房源', '本月签约总业绩（元）', '本月实收业绩（元）']
    if request.method == 'GET':
        return render_template('index.html')
    else :
        dot = re.compile('\d\.')
        word = request.form['word'].replace(' ', '').replace('\r', '').replace('天', '日').replace('（', '').replace('）', '')
        word = re.subn('\d\.', '', word)[0]
        word = word.split('\n')
        word = [ i for i in word if len(i) != 0 ]
        word = word[1:]

        match = []
        keys = []
        for line in biao:
            line = set(line)

            tmp = []
            key = 0
            for k,item in enumerate(word):
                item = set(item)
                if len(line & item) > len(tmp):
                    if not ('明' in line and '今' in item) or ('今' in line and '明' in item):
#                        print(line,item,line&item)
                        tmp = list(line & item)
                        key = k
#            print(tmp)
            match.append(tmp)
            keys.append(key)
#        print(match, keys)
#        print(word)

        wordList = []
        for k,key in enumerate(keys):
            tmp = word[key]
            for letter in match[k]:
                tmp = tmp.replace(letter, '<a>'+letter+'</a>')
                biao[k] = biao[k].replace(letter, '<a>'+letter+'</a>')
            wordList.append(tmp)
#        print(biao)
#        print(wordList)
#        print(match)

        return render_template('index.html', biao=biao, word=wordList, keys=keys)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
