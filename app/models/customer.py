# app/models/customer.py
from app.extensions import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    customer_username = db.Column(
        db.String(50), unique=True, nullable=False
    )

    name = db.Column(db.String(100), nullable=False)

    phone = db.Column(db.String(20), nullable=True)   # NOT unique
    email = db.Column(db.String(120), nullable=True) # NOT unique

    address = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    measurements = db.relationship("Measurement", backref="customer")
    orders = db.relationship("TailoringOrder", backref="customer")
