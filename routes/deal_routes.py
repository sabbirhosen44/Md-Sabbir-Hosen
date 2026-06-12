from flask import request
from flask import jsonify
from flask import Blueprint
from services.deal_service import create_deal, get_all_deals, get_single_deal

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
