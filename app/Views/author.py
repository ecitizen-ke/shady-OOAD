from flask import Blueprint, jsonify, request
from app.Models.Author import Author

author_bp = Blueprint("author_bp", __name__)


@author_bp.route("/api/authors")
def fetch_authors():
    author = Author()
    return jsonify({"authors": author.get_authors()}), 200


@author_bp.route("/api/store", methods=["POST"])
def store_author():
    email = request.get_json().get("email")
    name = request.get_json().get("name")
    if not email or not name:
        return jsonify({"error": True, "message": "Please provide email and name"}), 400
    else:
        author = Author()
        author.create_author(name, email)
        return jsonify({"author": author}), 201


@author_bp.route("/api/update/<int:id>", methods=["PATCH"])
def update_author(id):
    email = request.get_json().get("email")
    name = request.get_json().get("name")
    author_obj = Author()
    if not email or not name:
        return jsonify({"error": True, "message": "Please provide email and name"}), 400
    else:
        author = {}
        author["email"] = email
        author["name"] = name
        author_obj.update_author(id, author)
        return jsonify({"author": author}), 200


@author_bp.route("/api/delete/<int:id>", methods=["DELETE"])
def delete_author(id):

    author_obj = Author()
    author = author_obj.delete_author(id)
    if author != None:
        return jsonify({"error": True, "message": "Author was not found"}), 404
    else:

        return jsonify({"author": author}), 200
