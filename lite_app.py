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

    #all_charity = []
#     for charity_id,	accountability_score,	administrative_expenses,	charity_name,	charity_url,	city, cn_advisory,compensation_leader_compensation,	compensation_leader_expense_percent, compensation_leader_title, excess_or_deficit_for_year,	financial_score,	fundraising_expenses,	net_assets,	organization_type, other_revenue,	overall_score,	payments_to_affiliates,	program_expenses,	state_abbr, total_contributions, lat, lng in results:
 
#         charity_dict = {}
#         charity_dict["charity_id"] = charity_id

#         all_charity.append(charity_dict)

#     return jsonify(all_charity)
# engine = create_engine('sqlite:///Charity.sqlite')
# conn = engine.connect()
# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
# Base.classes.keys()
# # Save reference to the table
# Charity = pd.read_sql("select * from Charity",conn)



# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)

# #################################################
# # Flask Routes
# #################################################
# @app.route("/")
# def welcome():
#     """List all available charity data routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/charity"
#     )
# @app.route("/api/v1.0/charity")
# def charity():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     # engine = create_engine('sqlite:///Charity.sqlite', echo=True)
#     # sqlite_connection = engine.connect()
#     # sqlite_table = "Charity"
#     # charity_df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
#     # sqlite_connection.close()

#     """Return a list of Charity data"""
#     # Query all passengers
    
    
#     results = session.query(Charity.charity_id,	Charity.accountability_score,	Charity.administrative_expenses,	Charity.charity_name,\
#         	Charity.charity_url,	Charity.city,	Charity.cn_advisory,\
#         	Charity.compensation_leader_compensation,	Charity.compensation_leader_expense_percent,	Charity.compensation_leader_title,\
#                 	Charity.excess_or_deficit_for_year,	Charity.financial_score,	Charity.fundraising_expenses,	\
#                         Charity.net_assets,	Charity.organization_type,\
#                         	Charity.other_revenue,	Charity.overall_score,	Charity.payments_to_affiliates,	\
#                                 Charity.program_expenses,	Charity.state_abbr,\
#                                 	Charity.total_contributions,	Charity.lat,	Charity.lng).all()

#     session.close()
#     col_name = [charity_id,	accountability_score,	administrative_expenses,	charity_name,	charity_url,	city,\
#         cn_advisory,compensation_leader_compensation,	compensation_leader_expense_percent, compensation_leader_title,\
#             	excess_or_deficit_for_year,	financial_score,	fundraising_expenses,	net_assets,	organization_type,\
#                     	other_revenue,	overall_score,	payments_to_affiliates,	program_expenses,	state_abbr,\
#                             	total_contributions,	lat,	lng]
#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_charity = []
#     for charity_id,	accountability_score,	administrative_expenses,	charity_name,	charity_url,	city, cn_advisory,compensation_leader_compensation,	compensation_leader_expense_percent, compensation_leader_title, excess_or_deficit_for_year,	financial_score,	fundraising_expenses,	net_assets,	organization_type, other_revenue,	overall_score,	payments_to_affiliates,	program_expenses,	state_abbr, total_contributions, lat, lng in results:
 
#         charity_dict = {}
#         charity_dict["charity_id"] = charity_id

#         all_charity.append(charity_dict)

#     return jsonify(all_charity)


if __name__ == '__main__':
    app.run(debug=True)

