from flask import current_app, jsonify
from datetime import datetime

from app.model.certificados import Certificado

def create_certification(data):

    new_data = Certificado(**data)

    session = current_app.db.session

    new_data.expirated_at = datetime.fromtimestamp(new_data.expirated_at) 
    new_data.created_at = datetime.fromtimestamp(new_data.created_at)
    new_data.updated_at = datetime.fromtimestamp(new_data.updated_at)
 
    session.add(new_data)
    session.commit()
    
    return {
        "id": new_data.id,
        "username": new_data.username,
        "name": new_data.name,
        "description": new_data.description,
        "groups": new_data.groups,
        "expiration": new_data.expiration,
        "expirated_at":  new_data.expirated_at,
        "created_at": new_data.created_at,
        "updated_at": new_data.updated_at
   }

def delete_cert(id):
    session = current_app.db.session
    Certificado.query.filter_by(id=id).delete()

    session.commit()

def update_cert(id,req):
    session = current_app.db.session

    dados = Certificado.query.filter_by(id=id).first()

    for key, value in req.items():
        setattr(dados,key,value)

    dados.expirated_at = datetime.fromtimestamp(dados.expirated_at) 
    dados.created_at = datetime.fromtimestamp(dados.created_at)
    dados.updated_at = datetime.fromtimestamp(dados.updated_at)
    
    session.commit()

    return {
        "id": dados.id,
        "username": dados.username,
        "name": dados.name,
        "description": dados.description,
        "groups": dados.groups,
        "expiration": dados.expiration,
        "expirated_at":dados.expirated_at,
        "created_at": dados.created_at,
        "updated_at": dados.updated_at,
    }


def list_cert():
    data = Certificado.query.all()
    datas = [ {
        "id": item.id,
        "username": item.username,
        "name": item.name,
        "description": item.description,
        "groups": item.groups,
        "expiration": item.expiration,
        "expirated_at":item.expirated_at,
        "created_at": item.created_at,
        "updated_at": item.updated_at,
    }
    for item in data ]

    return jsonify(datas)
