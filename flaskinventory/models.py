from flaskinventory import db
from datetime import datetime

class Location(db.Model):
    loc_id = db.Column(db.Integer, primary_key= True)
    loc_name = db.Column(db.String(20),unique = True, nullable = False)

    def __repr__(self):
        return f"Location('{self.loc_id}','{self.loc_name}')"
        return "Location('{self.loc_id}','{self.loc_name}')"

class Product(db.Model):
    prod_id = db.Column(db.Integer, primary_key= True)
    prod_created_ts = db.Column(db.DateTime, default=datetime.utcnow)
    prod_updated_ts = db.Column(db.DateTime, nullable = True)
    prod_name = db.Column(db.String(20), nullable = False)
    prod_name = db.Column(db.String(20),unique = True ,nullable = False)
    prod_tqty = db.Column(db.Integer, nullable = False)
    prod_qty = db.Column(db.Integer, nullable = False)
    prod_dept = db.Column(db.Integer, nullable = False)
    prod_fnsh = db.Column(db.Integer, nullable = True)
    
    def __repr__(self):
        return f"Product('{self.prod_id}','{self.prod_created_ts}','{self.prod_update_ts}','{self.prod_name}','{self.prod_tqty}','{self.prod_qty}','{self.prod_dept}','{self.prod_fnsh}')"

class Movement(db.Model):
    mid = db.Column(db.Integer, primary_key= True)
    ts = db.Column(db.DateTime, default=datetime.utcnow)
    frm = db.Column(db.String(20), nullable = False)
    to = db.Column(db.String(20), nullable = False)
    pname = db.Column(db.String(20), nullable = False)
    pqty = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Movement('{self.mid}','{self.ts}','{self.frm}','{self.to}','{self.pname}','{self.pqty}')"

class Balance(db.Model):
    bid = db.Column(db.Integer, primary_key= True,nullable = False)
    product = db.Column(db.String(20), nullable = False)
    location = db.Column(db.String(20),nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Balance('{self.bid}','{self.product}','{self.location}','{self.quantity}')"

class Expense(db.Model):

    eid = db.Column(db.Integer, primary_key= True,nullable = False)
    ets = db.Column(db.DateTime, default=datetime.utcnow)
    e_person = db.Column(db.String(20), nullable = False)
    e_place = db.Column(db.String(20),nullable = False)
    e_cost = db.Column(db.Integer, nullable = False)
    e_quantity = db.Column(db.Integer, nullable= True)

    def __repr__(self):
        return f"Expense('{self.eid}','{self.ets}','{self.e_person}','{self.e_place}','{self.e_cost}','{self.e_quantity}')"