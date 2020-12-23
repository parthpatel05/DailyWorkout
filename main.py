from flask import Flask, redirect, url_for, request, session, flash, render_template
from datetime import datetime

app = Flask(__name__)

weekDict = {
    0:'monday',
    1:'tuesday',
    2:'wednesday',
    3:'thursday',
    4:'friday',
    5:'saturday',
    6:'sunday'

}

@app.route('/')
def home():
    now = datetime.today().weekday()
    nowTime = datetime.now()
    return render_template('home.html', day = weekDict[now], time = nowTime)

@app.route('/sunday')
def sunday():
    return render_template('sunday.html')

@app.route('/monday')
def monday():
    return render_template('monday.html')

@app.route('/tuesday')
def tuesday():
    return render_template('tuesday.html')

@app.route('/wednesday')
def wednesday():
    return render_template('wednesday.html')

@app.route('/thursday')
def thursday():
    return render_template('thursday.html')

@app.route('/friday')
def friday():
    return render_template('friday.html')

@app.route('/saturday')
def saturday():
    return render_template('saturday.html')

if __name__ == '__main__':
    app.run(debug=True)
