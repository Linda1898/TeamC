from application import db
from dataclasses import dataclass

@dataclass
class Quantity(db.Model):
    # the declarations below are important for turning the object into JSON
    quantity_id: int
    quantity: str
    measurement: str

    quantity_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'), nullable=False)
    quantity = db.Column(db.String(10))
    measurement = db.Column(db.String(10))