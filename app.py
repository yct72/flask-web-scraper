from flask import Flask, render_template
from db import *
import pymongo


app = Flask(__name__)


def get_data():
    coll = access_db()
    data = []
    for i in coll.find({}, {"_id":0}):
        data.append(i)
    return data


@app.route('/')
def index():
    print(get_data(), len(get_data()))
    return render_template("index.html", data=get_data(), threaded=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9092)
