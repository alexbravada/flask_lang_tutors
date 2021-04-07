import flask

from flask import Flask, render_template, request


app = Flask(__name__)
app.debug = True


# main page
@app.route('/')
def render_index():
    return render_template('index.html',)


app.run(debug=True)
