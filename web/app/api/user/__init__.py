from web.app.api.user.user import user_blueprint
from web.app.commons.utils.blueprint_wrapper import BlueprintWrapper

__blueprints = [user_blueprint]
user_blueprints = BlueprintWrapper(__blueprints, "/user")
