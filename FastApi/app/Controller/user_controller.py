from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models.user_model import User

@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email
    }), 200

@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data = request.get_json()

    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)

    db.session.commit()
    return jsonify({"message": "Profile updated successfully"}), 200

@jwt_required()
def delete_account():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Account deleted successfully"}), 200
