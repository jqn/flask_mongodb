from . import api

VERSION = "1.0"


@api.route(f'{VERSION}/users', methods=['POST'])
def create_user():
    pass
