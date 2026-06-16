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
    view_count = db.Column(db.Integer, default=0)
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
            "view_count": self.view_count,
            "last_viewed_at": (
                self.last_viewed_at.isoformat() if self.last_viewed_at else None
            ),
        }


class SearchHistory(db.Model):
    __tablename__ = "search_history"

    id = db.Column(db.Integer, primary_key=True)

    destination = db.Column(db.String(100), unique=True, nullable=False)

    search_count = db.Column(db.Integer, default=0)


class ApiStatistic(db.Model):
    __tablename__ = "api_statistics"

    id = db.Column(db.Integer, primary_key=True)

    total_requests = db.Column(db.Integer, default=0)

    successful_requests = db.Column(db.Integer, default=0)

    failed_requests = db.Column(db.Integer, default=0)
