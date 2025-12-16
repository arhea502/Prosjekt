from flask import Flask, render_template
from db import hentdata



app = Flask(__name__)

@app.route("/")
def home():
    data = hentdata()
    return render_template('index2.html', products = data) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)