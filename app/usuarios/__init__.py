from flask import Blueprint
usuarios = Blueprint('usuarios',
                     __name__,
                     url_prefix='/usuarios',
                     template_folder='templates')

from . import routes