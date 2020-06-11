import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
from flask import g, request, jsonify, after_this_request, render_template
from flask import Flask
#import numpy as np
#from datetime import datetime, timedelta
#import pandas as pd
import os

#charity_data=pd.read_sql("select * from charity",conn)
#database = './data/Charity_new.sqlite'
database = os.path.join(".","data","Charity_new.sqlite")

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    db.row_factory = sqlite3.Row

    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/paras')
def paras():
    parNames=['total_contributions','admin_expenses','leader_compensation','program_expenses','fundraising_expenses']
    return jsonify(parNames)

@app.route('/metrics')
def metrics():
    
    metrics_data = []
    columns = ['charity_name', 'city', 'state_abbr', 'organization_type', 'overall_score', 'administrative_expenses', 'compensation_leader_compensation', 'total_contributions', 'charity_id']
    #metric = query_db('select charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions, charity_id from Charity order by charity_name')   
    for metric in query_db('select charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions, charity_id from Charity order by charity_name'):
    
    
        metrics_data.append(dict(zip(columns, metric)))
 
    return jsonify(metrics_data)

@app.route('/ranking')
def ranking():
    #cur = get_db().cursor()
    metrics_data = []
    columns = ['charity_name', 'city', 'state_abbr', 'organization_type', 'overall_score', 'administrative_expenses', 'compensation_leader_compensation', 'total_contributions', 'fundraising_expenses','program_expenses','charity_id']
    #metric = query_db('select charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions, charity_id from Charity order by charity_name')
    for metric in query_db('select charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions, program_expenses, fundraising_expenses, charity_id from Charity order by charity_name'):
        metrics_data.append(dict(zip(columns, metric)))
    return jsonify(metrics_data)

@app.route('/names')
def org():
    orgNames = ['International', 'Human Services', 'Environment', 'Education',
       'Human and Civil Rights', 'Health', 'Animals',
       'Community Development', 'Religion',
       'Arts, Culture, Humanities', 'Research and Public Policy']

    return jsonify(orgNames)

@app.route('/location')
def locs():
    #cur = get_db().cursor()
    charity_names = []
    lat = []
    lng = []
    locations_data= []
    columns = ['charity_name', 'lat', 'lng', 'city']
    for location in query_db('select charity_name, lat, lng, city from Charity order by charity_name'):
        locations_data.append(dict(zip(columns, location)))
        

    return jsonify(locations_data)




@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/metricspage")
def metrics_page():
    """Metrics Page"""
    return render_template("metrics.html")



@app.route("/map")
def us_map():
    """US Map page"""
    return render_template("map.html")

@app.route("/rank")
def rank():
    """US Rankings page"""
    return render_template("rankings.html")



if __name__ == '__main__':
    app.run(debug=True)