#Eigenentwicklung
from app import app
from app.models import User, Cars
from flask import jsonify

@app.route('/api/users/<id>', methods=['GET'])
def get_users(id):
    data = User.query.get_or_404(id).to_dict()
    return jsonify(data)

@app.route('/api/users', methods=['GET'])
def get_users2():
    data = User.to_collection()
    return jsonify(data)

@app.route('/api/cars/<id>', methods=['GET'])
def get_cars(id):
    data2 = Cars.query.get_or_404(id).to_dict()
    return jsonify(data2)

@app.route('/api/cars', methods=['GET'])
def get_cars2():
    data2 = Cars.to_collection()
    return jsonify(data2)
