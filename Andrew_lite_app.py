import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
from flask import g, request, jsonify, after_this_request, Flask, render_template
import numpy as np
from datetime import datetime, timedelta
import pandas as pd

#charity_data=pd.read_sql("select * from charity",conn)
database = './data/Charity_new.sqlite'

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

@app.route('/metrics')
def metrics():
    #cur = get_db().cursor()
    scores = []
    charity_names = []
    city = []
    state = []
    organization_type = []
    scores = []
    admin_exp = []
    leader_comp = []
    total_cont = []
    charity_id = []
    for metric in query_db('select charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions, charity_id from Charity order by charity_name'):
       #print(metric)
       charity_names.append(metric["charity_name"])
       city.append(metric["city"])
       state.append(metric["state_abbr"])
       organization_type.append(metric["organization_type"])
       scores.append(metric["overall_score"])
       admin_exp.append(metric["administrative_expenses"])
       leader_comp.append(metric["compensation_leader_compensation"])
       total_cont.append(metric["total_contributions"])
       charity_id.append(metric["charity_id"])
    metrics_data = {}
    metrics_data["charity_name"] = charity_names
    metrics_data["city"] = city
    metrics_data["state"] = state
    metrics_data["organization_type"] = organization_type
    metrics_data["scores"] = scores
    metrics_data["admin_expenses"] = admin_exp
    metrics_data["leader_compensation"] = leader_comp
    metrics_data["total_contributions"] = total_cont
    metrics_data["charity_id"] = charity_id  
    return jsonify(metrics_data)

@app.route('/names')
def org():
    orgNames = ['International ', 'Human Services ', 'Environment ', 'Education ',
       'Human and Civil Rights ', 'Health ', 'Animals ',
       'Community Development ', 'Religion ',
       'Arts, Culture, Humanities ', 'Research and Public Policy ']

    return jsonify(orgNames)

@app.route('/location')
def locs():
    #cur = get_db().cursor()
    charity_names = []
    lat = []
    lng = []
    for location in query_db('select charity_name, lat, lng from Charity order by charity_name'):
        charity_names.append(location["charity_name"])
        lat.append(location["lat"])
        lng.append(location["lng"])

    locations_data = {}
    locations_data["charity_name"] = charity_names
    locations_data["latitude"] = lat
    locations_data["longitude"] = lng

    return jsonify(locations_data)

@app.route('/ranking/<organization>')
def ranking(organization):
    #cur = get_db().cursor()
    organization = "Animals "
    scores = []
    charity_names = []
    city = []
    state = []
    organization_type = []
    scores = []
    admin_exp = []
    leader_comp = []
    total_cont = []
    charity_id = []
    charities = query_db('select distinct charity_id, charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions from Charity where organization_type = ?', (organization,), one=False)
    for rank in charities: #query_db('select charity_id, charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions from Charity where organization_type = ?', (org,), one=True):
        print(rank)
        charity_id.append(rank["charity_id"])
        charity_names.append(rank["charity_name"])
        city.append(rank["city"])
        state.append(rank["state_abbr"])
        organization_type.append(rank["organization_type"])
        scores.append(rank["overall_score"])
        admin_exp.append(rank["administrative_expenses"])
        leader_comp.append(rank["compensation_leader_compensation"])
        total_cont.append(rank["total_contributions"])
    rankings_data = {}
    rankings_data["charity_id"] = charity_id
    rankings_data["charity_name"] = charity_names
    rankings_data["city"] = city
    rankings_data["state"] = state
    rankings_data["organization_type"] = organization_type
    rankings_data["scores"] = scores
    rankings_data["admin_expenses"] = admin_exp
    rankings_data["leader_compensation"] = leader_comp
    rankings_data["total_contributions"] = total_cont
    return jsonify(rankings_data)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/metricspage")
def metrics_page():
    """Metrics Page"""
    return render_template("metrics.html")

@app.route("/scatter")
def scatter_page():
    """Scatter Page"""
    return render_template("scatter.html")

@app.route("/usmap")
def us_map():
    """US Map page"""
    return render_template("usmap.html")

if __name__ == '__main__':
    app.run(debug=True)