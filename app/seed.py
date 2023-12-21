from faker import Faker
from models import Hero, Power, HeroPower,db
import random
from app import app 

fake = Faker()

with app.app_context():

    db.session.query(Hero).delete()
    db.session.query(Power).delete()
    db.session.query(HeroPower).delete()

    heroes = []
    for _ in range(10):  
        hero = Hero(
            name=fake.name(),
            super_name=fake.word()
        )
        heroes.append(hero)

    db.session.add_all(heroes)
    db.session.commit()

    powers = []
    for _ in range(10):
        power = Power(
            name=fake.word(),
            description='No power assigned yet'
            
        )
        powers.append(power)

    db.session.add_all(powers)
    db.session.commit()

    # Generate associations (HeroPower)
    hero_powers = []
    elements=['Strong', 'Weak', 'Average']
    for _ in range(20):
        hero_power = HeroPower(
            strength=random.choice(elements),
            hero_id=random.choice(heroes).id,
            power_id=random.choice(powers).id
        )
        hero_powers.append(hero_power)

    db.session.add_all(hero_powers)
    db.session.commit()
