from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    time = datetime.datetime.now()
    currenthour = time.hour
    if 6 <= currenthour < 12:
        return "Hello World! Good morning"
    elif 12 <= currenthour < 18:
        return "Hello World! Good afternoon"
    else:
        return "Hello World! Good night"
    
