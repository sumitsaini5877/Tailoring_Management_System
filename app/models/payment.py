# app/models/payment.py
from app.extensions import db

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)

    payment_type = db.Column(
        db.String(30), nullable=False
    )
    # advance, partial, full

    payment_mode = db.Column(db.String(30))  # cash, upi, card

    payment_date = db.Column(
        db.DateTime, server_default=db.func.now()
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("tailoring_orders.id"),
        nullable=False
    )
