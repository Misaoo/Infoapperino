from flask import Flask, flash, redirect, render_template, request, session
import os
import time
import config
import app

ap = Flask(__name__)

@ap.route('/bloggpost')
def create_post():
    return ''




if __name__ == "__main__":
    ap.secret_key = os.urandom(12)
    ap.run(debug=True)