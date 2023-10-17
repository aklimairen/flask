#!python 3.10
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_view():
    return "Wellcome to flask world main view!!!"


@app.route("/home")
def home_view():
    return "Wellcome to flask world home view!!!"


@app.route("/home/room")
def room_view():
    return "Wellcome to flask world room view!!!"

app.run()