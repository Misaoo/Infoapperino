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

app.debug=True

if __name__ == '__main__':
    app.run()
