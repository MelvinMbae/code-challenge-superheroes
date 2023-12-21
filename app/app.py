#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, HeroPower,Hero, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact=False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to our API'

@app.route('/heroes', methods=['GET'])
def get_all_heroes():
    
    heroes_dict=[hero.to_dict() for hero in Hero.query.all()]
    response=make_response(
        jsonify(heroes_dict),
        200
        )
    
    return response

@app.route('/heroes/<int:id>', methods=['GET'])
def get_singe_hero_by_id(id):
    
    if request.method=='GET':
        hero=Hero.query.filter(Hero.id==id).first()
        
        if hero ==None:
            response=make_response(
                jsonify({
                    "error": "Hero not found"
                }),404
            )
            return response
            
        
        elif hero:    
            response=make_response(
                jsonify(hero.to_dict()),
                200
                )
        
            return response
        
@app.route('/powers/<int:id>', methods=['GET'])
def get_singe_power_by_id(id):
    
    if request.method=='GET':
        power=Power.query.filter(Power.id==id).first()
        
        if power ==None:
            response=make_response(
                jsonify({
                    "error": "Power not found"
                }),404
            )
            return response
            
        
        elif power:    
            response=make_response(
                jsonify(power.to_dict()),
                200
                )
        
            return response
if __name__ == '__main__':
    app.run(port=5555, debug=True)
