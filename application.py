from flask import Flask, render_template, request, jsonify,redirect,url_for
import requests

app = Flask(__name__)
app_url = 'https://c8cdd0ab0585.ngrok.io'
app_data_file = 'payfast_data.txt'

@app.route("/")
def index():
    lines = open(app_data_file, 'r').read().split('\n')
    return render_template('index.html', app_url=app_url, purchase=lines)

@app.route("/clear")
def clear():
    f = open(app_data_file, "w")
    f.close()
    return redirect(url_for('index') , code=302)

@app.route("/receive_payment", methods=["GET", "POST"])
def receive_payment():
    data = request.get_data().decode().split('&')
    for i in range(0,len(data)):
        data[i] = data[i].split('=')
    f = open(app_data_file, "w")

    f.write("======================================================================================================\n")
    for key, val in data:
        f.write(f"{key} => {val}\n")

    f.write("======================================================================================================\n")
    f.close()
    return jsonify({'code': '200', 'result': "Success"})