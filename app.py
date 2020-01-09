from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize app
app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db = SQLAlchemy(app)

# Initialize ma
ma = Marshmallow(app)

# Incident Class/Model
class Incident(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(100))
  middle_name = db.Column(db.String(100))
  last_name = db.Column(db.String(100))
  grade = db.Column(db.String(10))
  class_period = db.Column(db.String(10))
  date_of_incident = db.Column(db.String(10))
  incident_type = db.Column(db.String(50))
  previous_intervention = db.Column(db.String(50))
  incident_description = db.Column(db.String(200))
  status = db.Column(db.String(10))
  resolution = db.Column(db.String(1000))

  def __init__(self,
               first_name,
               middle_name,
               last_name,
               grade,
               class_period,
               date_of_incident,
               incident_type,
               previous_intervention,
               incident_description,
               status,
               resolution):

    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.grade = grade
    self.class_period = class_period
    self.date_of_incident = date_of_incident
    self.incident_type = incident_type
    self.previous_intervention = previous_intervention
    self.incident_description = incident_description
    self.status = status
    self.resolution = resolution

# Incident Schema
class IncidentSchema(ma.Schema):
  class Meta:
    fields = ('id',
              'first_name',
              'middle_name',
              'last_name',
              'grade',
              'class_period',
              'date_of_incident',
              'incident_type',
              'previous_intervention',
              'incident_description',
              'status',
              'resolution')

# Initialize schema
incident_schema = IncidentSchema()
incidents_schema = IncidentSchema(many=True)

# Create Incident
@app.route('/incident', methods=['POST'])
def add_incident():
  first_name = request.json['first_name']
  middle_name = request.json['middle_name']
  last_name = request.json['last_name']
  grade = request.json['grade']
  class_period = request.json['class_period']
  date_of_incident = request.json['date_of_incident']
  incident_type = request.json['incident_type']
  previous_intervention = request.json['previous_intervention']
  incident_description = request.json['incident_description']
  status = request.json['status']
  resolution = request.json['resolution']

  new_incident = Incident(first_name,
                          middle_name,
                          last_name,
                          grade,
                          class_period,
                          date_of_incident,
                          incident_type,
                          previous_intervention,
                          incident_description,
                          status,
                          resolution)

  db.session.add(new_incident)
  db.session.commit()

  return incident_schema.jsonify(new_incident)

# Get all Incidents
@app.route('/incident', methods=['GET'])
def get_incidents():
  all_incident = Incident.query.all()
  result = incidents_schema.dump(all_incident)
  return jsonify(result)

# Get single Incident
@app.route('/incident/<id>', methods=['GET'])
def get_incident(id):
  incident = Incident.query.get(id)
  return incident_schema.jsonify(incident)

# Update Incident
@app.route('/incident/<id>', methods=['PUT'])
def update_incident(id):
  incident = Incident.query.get(id)

  first_name = request.json['first_name']
  middle_name = request.json['middle_name']
  last_name = request.json['last_name']
  grade = request.json['grade']
  class_period = request.json['class_period']
  date_of_incident = request.json['date_of_incident']
  incident_type = request.json['incident_type']
  previous_intervention = request.json['previous_intervention']
  incident_description = request.json['incident_description']
  status = request.json['status']
  resolution = request.json['resolution']

  incident.first_name = first_name
  incident.middle_name = middle_name
  incident.last_name = last_name
  incident.grade = grade
  incident.class_period = class_period
  incident.date_of_incident = date_of_incident
  incident.incident_type = incident_type
  incident.previous_intervention = previous_intervention
  incident.incident_description = incident_description
  incident.status = status
  incident.resolution = resolution

  db.session.commit()

  return incident_schema.jsonify(incident)

# Delete Incident
@app.route('/incident/<id>', methods=['DELETE'])
def delete_incident(id):
  incident = Incident.query.get(id)
  db.session.delete(incident)
  db.session.commit()

  return incident_schema.jsonify(incident)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
