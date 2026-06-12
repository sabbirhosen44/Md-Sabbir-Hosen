from database.db import db
from database.models import TravelDeal
from utils.validators import validate_deal


def create_deal(data):
    errors = validate_deal(data)

    if errors:
        return ({"success": False, "errors": errors}, 400)

    travel_deal = TravelDeal(
        destination=data["destination"],
        price=data["price"],
        platform=data["platform"],
        rating=data["rating"],
        travel_type=data["travel_type"],
    )

    db.session.add(travel_deal)
    db.session.commit()

    return {
        "success": True,
        "message": "Deal created successfully",
        "data": travel_deal.to_dict(),
    }, 201
