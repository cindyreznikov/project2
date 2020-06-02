import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
from flask import g, request, jsonify, after_this_request, Flask, render_template
import numpy as np
from datetime import datetime, timedelta
import pandas as pd
lite_app = Flask(__name__)

database = './data/Charity.sqlite'

engine = create_engine('sqlite:///Charity.sqlite')
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save reference to the table
Charity = pd.read_sql("select * from Charity",conn)



#################################################
# Flask Setup
#################################################
lite_app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@lite_app.route("/")
def welcome():
    """List all available charity data routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/charity"
    )
@lite_app.route("/api/v1.0/charity")
def charity():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # engine = create_engine('sqlite:///Charity.sqlite', echo=True)
    # sqlite_connection = engine.connect()
    # sqlite_table = "Charity"
    # charity_df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
    # sqlite_connection.close()

    """Return a list of Charity data"""
    # Query all passengers
    
    
    results = session.query(Charity.charity_id,	Charity.accountability_score,	Charity.administrative_expenses,	Charity.charity_name,\
        	Charity.charity_url,	Charity.city,	Charity.cn_advisory,\
        	Charity.compensation_leader_compensation,	Charity.compensation_leader_expense_percent,	Charity.compensation_leader_title,\
                	Charity.excess_or_deficit_for_year,	Charity.financial_score,	Charity.fundraising_expenses,	\
                        Charity.net_assets,	Charity.organization_type,\
                        	Charity.other_revenue,	Charity.overall_score,	Charity.payments_to_affiliates,	\
                                Charity.program_expenses,	Charity.state_abbr,\
                                	Charity.total_contributions,	Charity.lat,	Charity.lng).all()

    session.close()
    col_name = [charity_id,	accountability_score,	administrative_expenses,	charity_name,	charity_url,	city,\
        cn_advisory,compensation_leader_compensation,	compensation_leader_expense_percent, compensation_leader_title,\
            	excess_or_deficit_for_year,	financial_score,	fundraising_expenses,	net_assets,	organization_type,\
                    	other_revenue,	overall_score,	payments_to_affiliates,	program_expenses,	state_abbr,\
                            	total_contributions,	lat,	lng]
    # Create a dictionary from the row data and append to a list of all_passengers
    all_charity = []
    for charity_id,	accountability_score,	administrative_expenses,	charity_name,	charity_url,	city, cn_advisory,compensation_leader_compensation,	compensation_leader_expense_percent, compensation_leader_title, excess_or_deficit_for_year,	financial_score,	fundraising_expenses,	net_assets,	organization_type, other_revenue,	overall_score,	payments_to_affiliates,	program_expenses,	state_abbr, total_contributions, lat, lng in results:
 
        charity_dict = {}
        charity_dict["charity_id"] = charity_id

        all_charity.append(charity_dict)

    return jsonify(all_charity)


if __name__ == '__main__':
    lite_app.run(debug=True)

