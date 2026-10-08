# build 7ac60a3ce3
# (auto) eca49d
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
