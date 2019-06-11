# export FLASK_APP=application.py
# FLASK_DEBUG=1
# export DATABASE_URL=postgres://hjmhsjfzpjpavz:0aa7f77f38b4868fcd862900e8a61b7336ca81ce938cf93b608981acac76af21@ec2-23-21-106-241.compute-1.amazonaws.com:5432/ddehtv70ad62rh
# flask run
# api keys
# key: CpnTePb0hHYrY6126gfFdA
# secret: yEuqBseURUAmzsqp8hl6AOrunScczkyZWWaWg4mv60Y

import os
import requests
from flask import Flask, session ,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_in" )
def hello():
    return render_template("signin.html")

@app.route("/sign_up")
def hello1():   
    return "Signup"


@app.route("/next", methods=["POST"])
def m():
    user = request.form.get("name")
    pass1 = request.form.get("name1")

    valid=db.execute (" SELECT * FROM login_credentials WHERE username=:id AND passwords=:id_pass", {"id":user , "id_pass":pass1} ).fetchall()

    if valid:
        return render_template("next.html", username=user)
    
    return "wrong credetials_restart website"


@app.route("/result", methods=["POST" ,"GET"])
def m1():
    year = request.form.get("year")
    isbn = request.form.get("isbnn")
    title = request.form.get("titlee")
    author = request.form.get("authorr")
    result=db.execute ("SELECT * FROM books WHERE isbn=:get or author=:get1 or title=:get2  or year=:get3"  , {"get":isbn , "get1":author , "get2":title ,"get3" :year}).fetchall()
    return render_template("result.html", passing=result)


@app.route("/details" , methods=["POST"])
def m2():
    isbn=request.form.get("isbn")
    valid=db.execute("SELECT * FROM books WHERE isbn=:id " , {"id":isbn}).fetchall()
    res=requests.get("https://www.goodreads.com/book/review_counts.json",  params={"key":"CpnTePb0hHYrY6126gfFdA"  , "isbns": isbn})
    response= res.json()
    return render_template("details.html",pass1=valid , response=response)