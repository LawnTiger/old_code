from flask import Flask, render_template, request
import re
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def store():
    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
