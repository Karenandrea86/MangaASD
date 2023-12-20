from flask import Blueprint
mangas = Blueprint('mangas',
                    __name__,
                    url_prefix='/mangas',
                    template_folder='templates',
                    static_folder= 'images')

from . import routes