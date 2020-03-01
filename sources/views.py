from flask import render_template
from sources import app

@app.route('/')
def index():
    return render_template('index.html')