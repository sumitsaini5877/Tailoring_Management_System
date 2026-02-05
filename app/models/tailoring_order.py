
from app.extensions import db

class TailoringOrder(db.Model):
    __tablename__ = "tailoring_orders"

    id = db.Column(db.Integer, primary_key=True)

    dress_type = db.Column(db.String(50), nullable=False)

    order_date = db.Column(db.DateTime, server_default=db.func.now())
    delivery_date = db.Column(db.Date)

    total_amount = db.Column(db.Float, nullable=False)

    status = db.Column(
        db.String(30), default="pending"
    )
    # pending, in_progress, ready, delivered

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    measurement_id = db.Column(
        db.Integer,
        db.ForeignKey("measurements.id"),
        nullable=False
    )

    progress = db.relationship(
        "OrderProgress", backref="order", cascade="all, delete"
    )

    payments = db.relationship(
        "Payment", backref="order", cascade="all, delete"
    )
