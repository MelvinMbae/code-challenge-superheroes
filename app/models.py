from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    super_name=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())
    
    powers=db.relationship("HeroPower")
      
    def __repr__(self):
        return f"{self.name} with a super power name of {self.super_name}"
    
class Power(db.Model, SerializerMixin):
    __tablename__='powers'
    
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    description=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('description')
    def validate_description(self, key, description):
        if not description or len(description) < 20:
            raise ValueError('Description must be present and at least 20 characters long')
        return description
    # heroes=db.relationship('HeroPower')
    
    def __repr__(self):
        return f"{self.name} super power can be described as someone that has the power of {self.description}"
    
class HeroPower(db.Model, SerializerMixin):
    __tablename__='hero_powers'
    
    id=db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String)
    power_id=db.Column(db.Integer, db.ForeignKey("powers.id"))
    hero_id=db.Column(db.Integer, db.ForeignKey("heroes.id"))
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError('Strength must be one of: Strong, Weak, Average')
        return strength
    

    def __repr__(self):
        return f"{self.strength} belongs to super hero with ID: {self.hero_id}"
# add any models you may need.