from flask import Blueprint
prestamos = Blueprint('prestamos',
                     __name__,
                     url_prefix='/prestamos',
                     template_folder='templates')

from . import routes