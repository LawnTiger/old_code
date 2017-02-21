from flask import Flask
from flask import render_template
from flask import request

import re
from difflib import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else :
        dot = re.compile('\d\.')
        word = request.form['word'].replace(' ', '').replace('\r', '').replace(',', '\n')
        word = re.subn('\d\.', '', word)[0]
        word = word.split('\n')
        word = [ i for i in word if len(i) != 0 ]
        

        biao = ['今天录入房源', '月累计录入房源', '今日跟进房源', '今日录入客源', '月累计录入客源', '今日跟进客源', '今日实堪', '今日新增钥匙', '月累计新增钥匙', '今日网络端口新增', '今日买卖带看', '买卖还价', '月累计买卖带看', '今日租赁带看', '租赁还价', '月累计租赁带看', '今日经理陪看（个）', '今日在谈买卖单', '今日在谈租赁单', '预计明日成交买卖单', '预计明日成交租赁单', '今日一手主推项目', 'call客（个）', '今日派单', '今日一手意向客', '今日成交一手（套）', '明日到访一手意向客', '经理回访一手意向客', '预计明日成交一手（套）', '今日成交租赁（单）', '今日租单合同佣金', '今日租单实收佣金', '今日成交买卖（单）', '今日买卖合佣金', '今日买卖单实收佣金', '今日签独家房源', '今日成交独家房源', '本月累计买卖单', '本月累计租赁单', '本月累计签独家房', '本月累计成交独家房源', '本月签约总业绩（元）', '本月实收业绩（元）', '当月合同佣金目标', '完成率']
        test = HtmlDiff.make_file(HtmlDiff(), biao, word)
        print(word)
        return test
#        # test text
#        print(word)
#        match = re.findall('\d+人\d+张|\d+|《\S+》', word)
#        print(match, len(match))
#        return 'a'

        # str
#        pattern = re.compile('房源录入\d个')
#        match = pattern.search(word)
#        if match:
#            print(match.group())
#        else :
#            print('not found')
#        print(word)

        # list
        store = word[1:word.find('】')]
        wordList = word.split('\n')[1:]
        wordList = [ i for i in wordList if len(i) != 0]
        print(len(wordList))
        result = []
        for item in wordList:
            match = re.findall('\d+人\d+张|\d+|《\S+》', item)
            if match:
                for item in match:
                    result.append(item.replace('《', '').replace('》' ,''))
            else :
                # 输入数据漏掉 0
                result.append('0')

#        for i in range(0, len(wordList)):
#            if len(wordList[i]) == 0:
#                continue
#            match = re.findall('\d+|《\S+》', wordList[i])
#            if match:
#                for j in match:
#                    print(wordList[i])
#                    print(j)
#            else :
#                print(wordList[i])
#                print(0)

        print(result)
        print(biao)
        print(wordList)
        print(len(result))
        print(len(biao))
        print(len(wordList))

        return render_template('index.html', biao=biao, word=wordList, result=result)

if __name__ == '__main__':
    app.debug = True
#    app.host = '0.0.0.0'
    app.run(host='0.0.0.0')
