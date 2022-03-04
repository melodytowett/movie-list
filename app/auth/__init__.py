from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import new_view,forms