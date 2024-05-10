from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import create_engine, SQLAlchemy
from dotenv import load_dotenv
import os
import urllib

app = Flask(__name__)

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USR')
password = os.getenv('PWD')

driver = '{ODBC Driver 17 for SQL Server}'

odbc_str = 'DRIVER='+driver+';SERVER='+server+'PORT=1433;UID='+username+';DATABASE='+database+';PWD='+password
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.quote_plus(odbc_str)

app.config['SQLALCHEMY_DATABASE_URI'] = connect_str

db= SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  jeffid = db.Column(db.String(6))
  location = db.Column(db.String(100))
  testdate = db.Column(db.Date())
  testtime = db.Column(db.Date())

@app.route('/', methods=['GET'])
def home():
  return 'Hello to Fit Test'

@app.route('/users', methods=['GET'])
def get_users():
  try:
    users = Users.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except e:
    return make_response(jsonify({'message': 'error getting users'}), 500)






