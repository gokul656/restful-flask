from flask import Blueprint


class BlueprintWrapper:
    def __init__(self, blueprints: [Blueprint], url_prefix: str):
        self.__blueprints = blueprints
        self.__url_prefix = url_prefix

    def get_blueprints(self) -> Blueprint:
        return self.__blueprints

    def get_url_prefix(self) -> str:
        return self.__url_prefix
