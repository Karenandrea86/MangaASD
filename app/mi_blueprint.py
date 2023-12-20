from flask import Blueprint
mi_blueprint = Blueprint('mi_blueprint',
                        __name__,
                        url_prefix="/modulo")
@mi_blueprint.route('/ejemplo')
def ejemplo():
    return 'estoy en el modulo ejemplo'