from crypt import methods
from distutils.log import debug
from tkinter import PROJECTING
from flask import Flask


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "starting mahine learning PROJECTING"



if __name__=="__main__":
    app.run(debug=True)
