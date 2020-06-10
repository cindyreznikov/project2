# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Coord,Charity


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")


@app.route("/location")
def locs():
    results = db.session.query(Charity.charity_name, Coord.lat, Coord.lng, Coord_city).all()

    charity_name = [result[0] for result in results]
    lat = [result[1] for result in results]
    lng = [result[2] for result in results]
    city = [result[3] for result in results]
    pet_data = [{
        "charity_name": charity_name,
        "lat": lat,
        "lng": lng,
        "city": city
    }]

    return jsonify(pet_data)



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


if __name__ == "__main__":
    app.run()
