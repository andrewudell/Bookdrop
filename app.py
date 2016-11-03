from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/index')
def index():
    return render_template('index.html')

