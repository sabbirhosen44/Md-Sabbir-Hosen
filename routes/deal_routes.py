from flask import request
from flask import jsonify
from flask import Blueprint
from services.deal_service import (
    create_deal,
    get_all_deals,
    get_single_deal,
    search_travel_deals,
    filter_travel_deals,
    sort_travel_deals,
    get_recent_deals,
)

deal_bp = Blueprint("deal_bp", __name__)


# Create deal route
@deal_bp.route("/deals", methods=["POST"])
def add_deal():
    data = request.get_json()

    response, status = create_deal(data)

    return jsonify(response), status


# Get all deals route
@deal_bp.route("/deals", methods=["GET"])
def get_deals():
    response, status = get_all_deals()

    return jsonify(response), status


# Get a single deal route
@deal_bp.route("/deals/<int:deal_id>", methods=["GET"])
def get_deal(deal_id):
    response, status = get_single_deal(deal_id)

    return jsonify(response), status


# Search deals  route
@deal_bp.route("/deals/search", methods=["GET"])
def search_deals():
    destination = request.args.get("destination")
    platform = request.args.get("platform")
    travel_type = request.args.get("travel_type")

    response, status = search_travel_deals(destination, platform, travel_type)

    return jsonify(response), status


# Filter deals by budget route
@deal_bp.route("/deals/filter", methods=["GET"])
def filter_deals():
    min_price = request.args.get("min_price")

    max_price = request.args.get("max_price")

    response, status = filter_travel_deals(min_price, max_price)

    return jsonify(response), status


# Sort travel deals route
@deal_bp.route("/deals/sort", methods=["GET"])
def sort_deals():
    sort_by = request.args.get("sort_by")

    order = request.args.get(
        "order",
        "asc",
    )

    response, status = sort_travel_deals(
        sort_by,
        order,
    )

    return jsonify(response), status


# Get recently viewed deals
@deal_bp.route(
    "/deals/recent",
    methods=["GET"],
)
def recent_deals():
    response, status = get_recent_deals()

    return jsonify(response), status
