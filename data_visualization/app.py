#call env\Scripts\activate.bat
import os
from os import listdir
from os.path import isfile, join
from posixpath import split
from flask import Flask, render_template,url_for
import pandas as pd


app = Flask(__name__)

## INDEX
@app.route('/')
def index():
    return render_template('index.html')

## ABOUT
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__=='__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(debug=True)