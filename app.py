from __future__ import print_function,division
import sys
import os
import glob
import re
import numpy as np
from model import func
from model.db import search
from flask import Flask,url_for,redirect,request,render_template,jsonify

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        f=request.files['file']
        num=func(f)
        print(f"\n\n{num}\n\n")
        reclist=search(num)
        return redirect(url_for('upload',details=reclist))
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def upload():
    details=request.args.getlist('details',None)
    print(f"\n\n{details}\n\n")
    return render_template('details.html',details=details)

if __name__ == '__main__':
    app.run(debug=True)