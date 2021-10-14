from flask import Blueprint, request
from app.model.groups import Groups

from app.services.groups_services import create_groups

bp = Blueprint('groups',__name__, url_prefix='/api')

@bp.route('/groups', methods=['POST'])
def create():
    data = request.get_json()
    return create_groups(data),201
    
