# This is the main file #
from flask import Flask, render_template, send_file


app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def homepage():
#    return "Welcome to the accessible web development environment."
    return send_file("static/home.html")

if __name__ == "__main__":
    app.run(debug=True)