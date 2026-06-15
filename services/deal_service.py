from database.db import db
from database.models import TravelDeal
from utils.validators import validate_travel_deal
from utils.logger import logger


# Create a travel deal function
def create_deal(data):
    errors = validate_travel_deal(data)

    if errors:
        logger.error("Travel deal validation failed")
        return {
            "success": False,
            "message": "Validation failed",
            "data": {"errors": errors},
        }, 400

    travel_deal = TravelDeal(
        destination=data["destination"],
        price=data["price"],
        platform=data["platform"],
        rating=data["rating"],
        travel_type=data["travel_type"],
    )

    db.session.add(travel_deal)
    db.session.commit()

    logger.info(f"Travel deal created: {travel_deal.id}")

    return {
        "success": True,
        "message": "Deal created successfully",
        "data": travel_deal.to_dict(),
    }, 201


# Get all travel deals function
def get_all_deals():
    travel_deals = TravelDeal.query.all()

    logger.info("Retrieved all travel deals")

    return {
        "success": True,
        "message": "Travel deals retrieved successfully",
        "data": {
            "count": len(travel_deals),
            "travel_deals": [travel_deal.to_dict() for travel_deal in travel_deals],
        },
    }, 200


# Get a single travel deal function
def get_single_deal(deal_id):
    travel_deal = TravelDeal.query.get(deal_id)

    if not travel_deal:
        logger.error(f"Travel deal not found: {deal_id}")
        return {"success": False, "message": "Travel deal not found"}, 404

    return {
        "success": True,
        "message": "Travel deal retrieved successfully",
        "data": travel_deal.to_dict(),
    }, 200


# Search a travel deals
def search_travel_deals(destination, platform, travel_type):

    destination = destination.strip() if destination else None
    platform = platform.strip() if platform else None
    travel_type = travel_type.strip() if travel_type else None

    if not destination and not platform and not travel_type:
        logger.warning("Empty search request")
        return {
            "success": False,
            "message": "Provide at least one search parameter",
        }, 400

    query = TravelDeal.query

    if destination:
        query = query.filter(TravelDeal.destination.ilike(f"%{destination}%"))

    if platform:
        query = query.filter(TravelDeal.platform.ilike(f"%{platform}%"))

    if travel_type:
        query = query.filter(TravelDeal.travel_type.ilike(f"%{travel_type}%"))

    deals = query.all()

    logger.info("Search completed successfully")

    return {
        "success": True,
        "message": "Search completed successfully",
        "data": {
            "count": len(deals),
            "travel_deals": [deal.to_dict() for deal in deals],
        },
    }, 200
