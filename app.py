from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import sqlalchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///wdi.db'
db = SQLAlchemy(app)



class Indicator(db.Model):
    CountryName = db.Column(db.String(120), primary_key=True)
    CountryCode = db.Column(db.String(120))
    SeriesName= db.Column(db.String(120))
    SeriesCode= db.Column(db.String(120))
    YR2017= db.Column(db.String(120))
    YR2018= db.Column(db.String(120))

    def __init__(self, CountryName,  CountryCode, SeriesName, SeriesCode, YR2017, YR2018 ):
        self.CountryName = CountryName
        self.CountryCode = CountryCode
        self.SeriesName = SeriesName
        self.SeriesCode = SeriesCode
        self.YR2017 = YR2017
        self.YR2018 = YR2018


app_root = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(app_root, 'images/')

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/wdi')
def wdi():
    return render_template('wdi.html')

@app.route('/wdi/raw_data')
def raw_data():
    conn = sqlite3.connect('wdi.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM Indicator')
    rows = c.fetchall();
    Indicators = Indicator.query.all()
    return render_template('raw_data.html', rows = rows)

if __name__ == '__main__':
    app.run(debug=True)
