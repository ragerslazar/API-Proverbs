from flask import Blueprint, jsonify, request

from controllers.ProverbsController import ProverbsController

routes_proverbs = Blueprint("routes_proverbs", __name__)

proverbs_controller = ProverbsController()

@routes_proverbs.route("/<int:proverb_id>", methods=["GET"])
def get_proverb_by_id(proverb_id):
    result = proverbs_controller.getProverbById(proverb_id)
    if result:
        return jsonify(result), 200
    return jsonify({"error": f"No proverb found for ID {proverb_id}."}), 404


@routes_proverbs.route("/delete/<int:proverb_id>", methods=["DELETE"])
def delete_proverb_by_id(proverb_id):
    result = proverbs_controller.deleteProverbById(proverb_id)
    if result > 0:
        return jsonify({"success": f"Proverb {proverb_id} deleted."}), 200

    return jsonify({"error": f"No proverb found for ID {proverb_id}."}), 404

@routes_proverbs.route("/random", methods=["GET"])
def get_random_proverb():
    result = proverbs_controller.getRandomProverb()
    if result:
        return jsonify(result), 200
    return jsonify({"error": "No proverb found."})

@routes_proverbs.route('/', methods=['POST'])
def add_proverb():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Bad request."}), 400

    proverb = data.get("proverb")
    author = data.get("author")

    if not proverb or not author:
        return jsonify({"error": "Missing proverb or author."}), 400

    return jsonify({"success": "Proverb added."}), 201