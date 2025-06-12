from flask import Flask, render_template

app = Flask("potato")

@app.route('/')
def index():
    return 'potato'