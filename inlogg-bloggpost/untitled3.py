from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/blogpost')
def blogpost():
    return render_template('blogpost.html')




if __name__ == '__main__':
    app.run(debug=True)