from flask import Blueprint, jsonify, request

from web import db
from web.app.api.validations.user_validation import UserRegister
from web.app.models.user import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json()
        # validations
        UserRegister(**data)

        user = User(**data)
        db.session.add(user)
        db.session.commit()

        return jsonify({"status": "success", "data": request.json}), 200
    except Exception as e:
        db.session.rollback()
        raise Exception(e)
