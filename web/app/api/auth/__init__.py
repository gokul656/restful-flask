from web.app.api.auth.core import auth_blueprint
from web.app.commons.utils.blueprint_wrapper import BlueprintWrapper

__blueprint_list = [auth_blueprint]
auth_blueprints = BlueprintWrapper(__blueprint_list, "/auth")
