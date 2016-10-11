from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)


@app.route('/')
def hello_world(name=None):

    return render_template('index.html', name=name)


@app.route('/schema')
def schema(name=None):

    return render_template('schema.html', name=name)


@app.route('/blogpost')
def blogpost(name=None):

    return render_template('blogpost.html', name=name)


@app.route('/login')
def login(name=None):

    return render_template('login.html', name=name)


@app.route('/admin')
def admin(name=None):

    return render_template('admin.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
