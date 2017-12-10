# coding: utf-8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    data = {}
    return render_template('index.html', data=data)

@app.route('/convert', methods=['POST'])
def convert():
    data = {}

    origin_str = request.form['str']

    lines = origin_str.splitlines()

    idx = 0
    max_column_cnt = 0

    line_arr = []
    for line in lines:
        columns = line.split("\t")
        max_column_cnt = len(columns) if len(columns) > max_column_cnt else max_column_cnt
        line_arr.append(columns)

    ret_str = ""
    line_idx = 0
    for line in line_arr:
        if line_idx == 1:
            for i in range(max_column_cnt):
                if (max_column_cnt - 1) > i:
                    ret_str += "|---"
                else:
                    ret_str += "|\n"

        for i in range(max_column_cnt):
            line_str = ""
            if line[i] is not None:
                line_str = "|" + line[i]
            else:
                line_str = "|"
            ret_str += line_str
        line_idx+=1
        if len(line_arr) > line_idx:
            ret_str += "|\n"
        else:
            ret_str += "|"

    data["origin_str"] = origin_str
    data["convert_str"] = ret_str
    data["convert_str_esc"] = repr(ret_str)[1:-1]

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
