from flask import Flask,render_template
import pymongo
from pymongo import MongoClient
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import datetime
import pytz
import os
import string
import urllib3

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to group 5 Final Project</h1><h2>DATA PROGRAMMING - BIG DATA - BDAT 1004</h2>."
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/bar_chart")
def bar_chart():
    return render_template("bar_chart.html")

@app.route("/column_chart")
def Column_chart():
    return render_template("Column_chart.html")

@app.route("/pie_chart")
def pie_chart():
    return render_template("pie_chart.html")


client = MongoClient('mongodb+srv://akshattomar77:ZZp6vuAxAjqRDOLP@dp-final.sqtrdfc.mongodb.net/?retryWrites=true&w=majority')
db=client.get_database("DP_FINAL_PROJECT")

records= db.Rates


#print(records)

if __name__=="__main__":
    app.run(debug=True)

  
    url = "https://coinranking1.p.rapidapi.com/coins"
    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}
    headers = {
	"X-RapidAPI-Key": "ff1cbaa13bmsh023867f4e18e3a0p1b4b54jsn3a92154d1def",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    req = requests.get(url, headers=headers, params=querystring)

    if(req.status_code==200):
        x=0
        while(x<10):
            data = req.json()
            records.insert_one(data)
            print(req)
            time.sleep(60)
            ++x

    else:
        print(req.status_code)

