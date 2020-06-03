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
database = './data/Charity.sqlite'

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
    for metric in query_db('select charity_name, city, state_abbr, organization_type, overall_score, administrative_expenses, compensation_leader_compensation, total_contributions from Charity order by charity_name'):
       #print(metric)
       charity_names.append(metric["charity_name"])
       city.append(metric["city"])
       state.append(metric["state_abbr"])
       organization_type.append(metric["organization_type"])
       scores.append(metric["overall_score"])
       admin_exp.append(metric["administrative_expenses"])
       leader_comp.append(metric["compensation_leader_compensation"])
       total_cont.append(metric["total_contributions"])

    metrics_data = {}
    metrics_data["charity_name"] = charity_names
    metrics_data["city"] = city
    metrics_data["state"] = state
    metrics_data["organization_type"] = organization_type
    metrics_data["scores"] = scores
    metrics_data["admin_expenses"] = admin_exp
    metrics_data["leader_compensation"] = leader_comp
    metrics_data["total_contributions"] = total_cont   
    return jsonify(metrics_data)

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



if __name__ == '__main__':
    app.run(debug=True)