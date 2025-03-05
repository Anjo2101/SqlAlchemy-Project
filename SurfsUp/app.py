# Import the dependencies.
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return(
        f"Welcome! This is a Hawaii Exploration & Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the MM/DD/YYYY format.</p>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation data for the last year"""
    # Calculate data one year ago from last date in database
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= last_year).all()

    # Create dictionary with date as key and prcp as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = session.query(Station.station).all()

    # Unravel results into a 10 array and conver to a list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for last year."""
    # Calculate data one year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query primary station for last year tobs
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    
    # Unravel results into a 10 array and conver to a list
    temps = list(np.ravel(results))

    # return the results
    return jsonify(temps=temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TEMP(MIN), TEMP(AVG), TEMP(MAX)"""

    # select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:

        # Return a JSON list of the minimum temperature, the average temperature, 
        # and the maximum temperature for a specified start or start-end range.
        # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*sel).filter(Measurement.date >= start).all()

    # Unravel results into a 10 array and conver to a list
        temps = list(np.ravel(results))
        return jsonify(temps)
    # For a specified start date and end date, calculate TMIN, TAVG, and TMAX
    #  for the dates from the start date to the end date, inclusive.
    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")
    
    results = session.query(*sel).filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    # Unravel results into a 10 array and conver to a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


if __name__ == '__main__':
    app.run()