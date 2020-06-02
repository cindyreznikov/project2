# Dependencies
import requests
import json
import gmaps
import pandas as pd
# from config import api_key gkey
from pprint import pprint
import sqlite3 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import g, jsonify

database = './data/Charity.sqlite'

conn = sqlite3.connect(database)

#This is the important part, here we are setting row_factory property of
#connection object to sqlite3.Row(sqlite3.Row is an implementation of
#row_factory)
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from Charity')

result = c.fetchall()
print(result)
#returns a list of dictionaries, each item in list(each dictionary)
#represents a row of the table