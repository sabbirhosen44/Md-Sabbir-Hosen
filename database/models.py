# Database models definition.
# Defines the 'Deal' table structure and provides utility methods


from database.db import db


class TravelDeal(db.Model):
    __tablename__ = "deals"

    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    travel_type = db.Column(db.String(50), nullable=False)
    last_viewed_at = db.Column(db.DateTime, nullable=True)

    # to_dict() for JSON serialization.
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "price": self.price,
            "platform": self.platform,
            "rating": self.rating,
            "travel_type": self.travel_type,
            "last_viewed_at": (
                self.last_viewed_at.isoformat() if self.last_viewed_at else None
            ),
        }
