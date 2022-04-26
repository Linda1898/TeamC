from application import db
from dataclasses import dataclass

@dataclass
class FoodGroup(db.Model):
    # the declarations below are important for turning the object into JSON
    food_group_id: int
    group_name: str
    group_chart: str
    group_fact: str

    food_group_id: db.Column(db.Integer, primary_key=True)
    group_name: db.Column(db.String(20), nullable=False)
    group_chart: db.Column(db.String(50))
    group_fact: db.Column(db.String(500))
    # call these variables your own names don't worry about match
    food_item = db.relationship('FoodItem', backref='food_item')
    # TODO: saving tinyblobs as (db.String(50) but this needs checking

    # save url as a str for pics (as in the link to the picture). Or have a folder in static and  save the name of the pic to be displayed.