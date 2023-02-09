from datetime import datetime
from flask import Flask, render_template, request, redirect
from . import app
from werkzeug.utils import secure_filename
import json
from collections import OrderedDict

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return "test"
    # return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route('/review_model', methods=['GET','POST'])
def index():     
    result = "wwwwoooowwww"
    
    if request.method == 'POST':
        print(request.method)
        f = request.files['files']
        fname = f.filename
        # f.filename = 8885_2023-02-02_14시04분.m4a

        file_data = OrderedDict()
        # 핸드폰 번호
        file_data["phoneNum"] = fname[0:-22]
        # 통화 날짜
        file_data["when"] = fname[-21:-11]
        # 통화 시각
        hh, mm = int(fname[-10:-8]), fname[-7:-5]
        if (hh > 12):
                hh = hh - 12
                ampm = "오후"
        else:
            ampm = "오전"
        hh = str(hh)
        file_data["duration"] = ampm + " " + hh + ":" + mm

        model_result = json.dumps(file_data, ensure_ascii=False, indent='\t')
        print(model_result)
        print(type(model_result))
        # print(fname)
        # print(file_data)

        # f.save(secure_filename(f.filename))
        result = model_result

    if request.method == 'GET':
        result = "get result"

    return result
