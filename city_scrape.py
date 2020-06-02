# Dependencies
import requests
import json
import gmaps
import pandas as pd
# from config import api_key gkey
from pprint import pprint
import sqlite3 
from flask import g

database = './data/Charity.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db
@app.teardown_appcontext
def close_connection(exception)
def