from flask import Blueprint, request

from app.model.certificados import Certificado
from app.services.certification_services import create_certification, delete_cert, list_cert, update_cert


bp = Blueprint('certification',__name__, url_prefix='/api')

@bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    print(data)
    return create_certification(data),201

@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    delete_cert(id)
    return  '',204

@bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    req = request.get_json()
    return update_cert(id,req),200

@bp.route('/list', methods=['GET'])
def list():
    return list_cert(),200
