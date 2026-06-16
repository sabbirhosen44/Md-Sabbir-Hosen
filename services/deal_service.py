from database.db import db
from database.models import TravelDeal
from utils.validators import (
    validate_travel_deal,
    validate_price_filter,
    TRAVEL_TYPES,
    normalize_search_param,
    validate_sort,
)
from utils.logger import logger
from datetime import datetime


# Create a travel deal function
def create_deal(data):
    errors = validate_travel_deal(data)

    if errors:
        logger.warning("Travel deal validation failed")
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

    travel_deal.last_viewed_at = datetime.utcnow()

    db.session.commit()

    logger.info(f"Viewed travel deal: {deal_id}")

    return {
        "success": True,
        "message": "Travel deal retrieved successfully",
        "data": travel_deal.to_dict(),
    }, 200


# Reusable search query builder
def build_search_query(
    destination=None,
    platform=None,
    travel_type=None,
):
    query = TravelDeal.query

    if destination:
        query = query.filter(TravelDeal.destination.ilike(f"%{destination}%"))

    if platform:
        query = query.filter(TravelDeal.platform.ilike(f"%{platform}%"))

    if travel_type:
        query = query.filter(TravelDeal.travel_type.ilike(f"%{travel_type}%"))

    return query


# Search a travel deals function
def search_travel_deals(destination, platform, travel_type):
    destination = normalize_search_param(destination)

    platform = normalize_search_param(platform)

    travel_type = normalize_search_param(travel_type)

    if not destination and not platform and not travel_type:
        logger.warning("Empty search request")

        return {
            "success": False,
            "message": "Provide at least one search parameter",
            "data": None,
        }, 400

    if travel_type and travel_type.title() not in TRAVEL_TYPES:
        logger.warning(f"Invalid travel type requested: {travel_type}")

        return {
            "success": False,
            "message": f"travel_type must be one of {TRAVEL_TYPES}",
            "data": None,
        }, 400

    deals = build_search_query(
        destination,
        platform,
        travel_type,
    ).all()

    logger.info("Search completed successfully")

    return {
        "success": True,
        "message": "Search completed successfully",
        "data": {
            "count": len(deals),
            "travel_deals": [deal.to_dict() for deal in deals],
        },
    }, 200


# Filter travel deals by budget function
def filter_travel_deals(
    min_price,
    max_price,
):
    errors = validate_price_filter(
        min_price,
        max_price,
    )

    if errors:
        logger.warning("Invalid filter request")

        return {
            "success": False,
            "message": "Validation failed",
            "data": {"errors": errors},
        }, 400

    query = TravelDeal.query

    if min_price is not None:
        min_price = float(min_price)

        query = query.filter(TravelDeal.price >= min_price)

    if max_price is not None:
        max_price = float(max_price)

        query = query.filter(TravelDeal.price <= max_price)

    deals = query.all()

    logger.info("Filter request completed")

    return {
        "success": True,
        "message": "Filter completed successfully",
        "data": {
            "count": len(deals),
            "travel_deals": [deal.to_dict() for deal in deals],
        },
    }, 200


# Sort travel deals function
def sort_travel_deals(sort_by, order):
    errors = validate_sort(
        sort_by,
        order,
    )

    if errors:
        logger.warning("Invalid sorting request")

        return {
            "success": False,
            "message": "Validation failed",
            "data": {"errors": errors},
        }, 400

    direction = TravelDeal.price.desc() if order == "desc" else TravelDeal.price.asc()

    deals = TravelDeal.query.order_by(direction).all()

    logger.info("Sorting completed successfully")

    return {
        "success": True,
        "message": "Sorting completed successfully",
        "data": {
            "count": len(deals),
            "travel_deals": [deal.to_dict() for deal in deals],
        },
    }, 200


# Get 5 recent viewed travel deals
def get_recent_deals():
    deals = (
        TravelDeal.query.filter(TravelDeal.last_viewed_at.isnot(None))
        .order_by(TravelDeal.last_viewed_at.desc())
        .limit(5)
        .all()
    )

    logger.info("Retrieved recently viewed deals")

    return {
        "success": True,
        "message": "Recently viewed deals retrieved successfully",
        "data": {
            "count": len(deals),
            "travel_deals": [deal.to_dict() for deal in deals],
        },
    }, 200


# Update a travel deal
def update_deal(deal_id, data):
    travel_deal = TravelDeal.query.get(deal_id)

    if not travel_deal:
        return {
            "success": False,
            "message": "Travel deal not found",
        }, 404

    errors = validate_travel_deal(data)

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
        }, 400

    travel_deal.destination = data["destination"]
    travel_deal.price = data["price"]
    travel_deal.platform = data["platform"]
    travel_deal.rating = data["rating"]
    travel_deal.travel_type = data["travel_type"]

    db.session.commit()

    logger.info(f"Travel deal updated: {deal_id}")

    return {
        "success": True,
        "message": "Travel deal updated successfully",
        "data": travel_deal.to_dict(),
    }, 200
