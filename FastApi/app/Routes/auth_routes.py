from flask import Blueprint
from ..controllers import auth_controller

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/register", methods=["POST"])(auth_controller.register)
auth_bp.route("/login", methods=["POST"])(auth_controller.login)
