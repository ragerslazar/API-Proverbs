from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from api.v1.controllers.ProverbsController import ProverbsController

routes_proverbs = Blueprint("routes_proverbs", __name__)
proverbs_controller = ProverbsController()

@routes_proverbs.route("/<int:proverb_id>", methods=["GET"])
def get_proverb_by_id(proverb_id):
    result = proverbs_controller.getProverbById(proverb_id)
    if result:
        return jsonify(result), 200
    return jsonify({
        "status": "failed",
        "error": f"No proverb found for ID {proverb_id}"
    }), 404


@routes_proverbs.route("/<int:proverb_id>", methods=["DELETE"])
@jwt_required()
def delete_proverb_by_id(proverb_id):
    result = proverbs_controller.deleteProverbById(proverb_id)
    if result is not None and result > 0:
        return jsonify({
            "status": "success",
            "message": f"Proverb {proverb_id} deleted"
        }), 200

    return jsonify({
        "status": "failed",
        "error": f"No proverb found for ID {proverb_id}"
    }), 404


@routes_proverbs.route("/random", methods=["GET"])
def get_random_proverb():
    result = proverbs_controller.getRandomProverb()
    if result:
        return jsonify(result), 200
    return jsonify({
        "status": "failed",
        "error": "No proverb found"
    }), 404


@routes_proverbs.route('/', methods=['POST'])
@jwt_required()
def add_proverb():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "failed",
            "error": "Bad request"
        }), 400

    proverb = data.get("proverb")
    author = data.get("author")

    if not proverb or not author:
        return jsonify({
            "status": "failed",
            "error": "Missing proverb or author."
        }), 400

    result = proverbs_controller.addProverb(proverb, author)
    if result is not None and result > 0:
        return jsonify({
            "status": "success",
            "message": "Proverb added"
        }), 201

    return jsonify({
        "status": "failed",
        "error": f"No proverb was added"
    }), 422