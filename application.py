from flask import Flask, render_template, request, jsonify
# import numpy as np
import requests

app = Flask(__name__)
app_url = 'http://63ec2666f911.ngrok.io'

@app.route("/")
def index():
    return render_template('index.html', app_url=app_url)

@app.route("/receive_payment", methods=["GET", "POST"])
def receive_payment():
    data = request.get_data().decode().split('&')
    for i in range(0,len(data)):
        data[i] = data[i].split('=')
    f = open("payfast_data.txt", "a")
    # f.write(data)

    f.write("======================================================================================================\n")
    for key, val in data:
        f.write(f"{key} => {val}\n")

    f.write("======================================================================================================\n")
    f.close()
    return render_template('forward.html', product=data)