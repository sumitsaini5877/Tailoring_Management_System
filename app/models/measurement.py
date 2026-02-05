
from app.extensions import db

class Measurement(db.Model):
    __tablename__ = "measurements"

    id = db.Column(db.Integer, primary_key=True)

    dress_type = db.Column(db.String(50), nullable=False)

    chest = db.Column(db.Float)
    waist = db.Column(db.Float)
    hip = db.Column(db.Float)
    shoulder = db.Column(db.Float)
    sleeve = db.Column(db.Float)
    length = db.Column(db.Float)

    notes = db.Column(db.Text)

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    created_at = db.Column(db.DateTime, server_default=db.func.now())
