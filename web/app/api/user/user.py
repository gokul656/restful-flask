from flask import Blueprint

from web.app.models.user import User

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/all", methods=["GET"])
def get_users():
    return [user.json() for user in User.query.all()]


@user_blueprint.route("/<email>", methods=["GET"])
def get_user_data(email: str):
    user = User.query.filter_by(email=email).first()
    if user is None:
        raise Exception("User not found!")

    return user.json()
