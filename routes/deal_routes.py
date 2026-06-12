from flask import request
from flask import jsonify
from flask import Blueprint
from services.deal_service import create_deal

deal_bp = Blueprint("deal_bp", __name__)


@deal_bp.route("/deals", methods=["POST"])
def add_deal():
    data = request.get_json()

    response, status = create_deal(data)

    return jsonify(response), status
