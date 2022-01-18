from flask import Flask
from bmr import *

app = Flask(__name__)

@app.route("/Home-Page")
def Home():
    return( "<h1>Home Page</h1>")
@app.route("/Bmr-calculator")
def bmr_app1():
    return (bmr_app())

if __name__ == "__main__":
    app.run()