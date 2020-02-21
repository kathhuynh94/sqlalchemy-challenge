from flask import Flask, json, jsonify
from db_prepare import engine, func, session, Measurement, Station
app = Flask(__name__)
@app.route('/')
def home_route():
    """ API routes"""
    return(
        f"Precipitation:<br/>"
        f"/api/v1.0/precipitation/ <br><br/>" 
        f"Stations:<br/>"
        f"/api/v1.0/stations/ <br><br/>" 
        f"Temperatures:<br/>"
        f"/api/v1.0/tobs/<br><br/>"
        f"Start date:  <br/>"
        f" /api/v1.0/2017-01-01/ <br><br/>" 
        f"Start and end date:  <br/>"
        f" /api/v1.0/2017-01-01/2018-12-31/ <br><br/>")
@app.route('/api/v1.0/precipitation/')
def precipitation():
    prcp_results = session.query(Measurement.date, Measurement.tobs)\
    .filter(Measurement.date >= '2017-01-01').all()
    p_dict = dict(prcp_results)
    session.close()
    return jsonify(p_dict) 
@app.route('/api/v1.0/stations/')
def stations():
    station_list = session.query(Station.station)\
    .order_by(Station.station).all() 
    for row in station_list:
        print (row[0])
    session.close()
    return jsonify(station_list)
@app.route('/api/v1.0/tobs/')
def tobs():
    temp_obs = session.query(Measurement.tobs)\
    .order_by(Measurement.date).all()
    session.close()
    return jsonify(temp_obs)
@app.route('/api/v1.0/<start>/')
def combined_start(start):
    q = session.query(
                  func.min(Measurement.tobs),
                  func.max(Measurement.tobs),
                  func.avg(Measurement.tobs))\
                  .filter(Measurement.station == Station.station)\
                  .filter(Measurement.date >= start).all()
    for row in q:
        print()
        print(row)
    session.close()
    return jsonify(q)
@app.route('/api/v1.0/<start_2>/<end>/')
def combined_start_end(start_2,end):
    q = session.query(
                  Measurement.date,
                  func.min(Measurement.tobs),
                  func.max(Measurement.tobs),
                  func.avg(Measurement.tobs))\
                    .group_by(Measurement.date)\
                  .filter(Measurement.station == Station.station)\
                  .filter(Measurement.date <= end)\
                  .filter(Measurement.date >= start_2).all()
    for row in q:
        print()
        print(row)
    start_end_dic = {}
    for date, min, max, avg in q:
        start_end_dic[date] = [min, max, avg]
        
    session.close()
    return jsonify(start_end_dic)
app.run(debug=True)from flask import Flask, json, jsonify
from db_prepare import engine, func, session, Measurement, Station
app = Flask(__name__)
@app.route('/')
def home_route():
    """ API routes"""
    return(
        f"Precipitation:<br/>"
        f"/api/v1.0/precipitation/ <br><br/>" 
        f"Stations:<br/>"
        f"/api/v1.0/stations/ <br><br/>" 
        f"Temperatures:<br/>"
        f"/api/v1.0/tobs/<br><br/>"
        f"Start date:  <br/>"
        f" /api/v1.0/2017-01-01/ <br><br/>" 
        f"Start and end date:  <br/>"
        f" /api/v1.0/2017-01-01/2018-12-31/ <br><br/>")
@app.route('/api/v1.0/precipitation/')
def precipitation():
    prcp_results = session.query(Measurement.date, Measurement.tobs)\
    .filter(Measurement.date >= '2017-01-01').all()
    p_dict = dict(prcp_results)
    session.close()
    return jsonify(p_dict) 
@app.route('/api/v1.0/stations/')
def stations():
    station_list = session.query(Station.station)\
    .order_by(Station.station).all() 
    for row in station_list:
        print (row[0])
    session.close()
    return jsonify(station_list)
@app.route('/api/v1.0/tobs/')
def tobs():
    temp_obs = session.query(Measurement.tobs)\
    .order_by(Measurement.date).all()
    session.close()
    return jsonify(temp_obs)
@app.route('/api/v1.0/<start>/')
def combined_start(start):
    q = session.query(
                  func.min(Measurement.tobs),
                  func.max(Measurement.tobs),
                  func.avg(Measurement.tobs))\
                  .filter(Measurement.station == Station.station)\
                  .filter(Measurement.date >= start).all()
    for row in q:
        print()
        print(row)
    session.close()
    return jsonify(q)
@app.route('/api/v1.0/<start_2>/<end>/')
def combined_start_end(start_2,end):
    q = session.query(
                  Measurement.date,
                  func.min(Measurement.tobs),
                  func.max(Measurement.tobs),
                  func.avg(Measurement.tobs))\
                    .group_by(Measurement.date)\
                  .filter(Measurement.station == Station.station)\
                  .filter(Measurement.date <= end)\
                  .filter(Measurement.date >= start_2).all()
    for row in q:
        print()
        print(row)
    start_end_dic = {}
    for date, min, max, avg in q:
        start_end_dic[date] = [min, max, avg]
        
    session.close()
    return jsonify(start_end_dic)
app.run(debug=True)