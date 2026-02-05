
from app.extensions import db

class OrderProgress(db.Model):
    __tablename__ = "order_progress"

    id = db.Column(db.Integer, primary_key=True)

    stage = db.Column(db.String(50), nullable=False)
    # cutting, stitching, fitting, ready

    remarks = db.Column(db.Text)

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("tailoring_orders.id"),
        nullable=False
    )
