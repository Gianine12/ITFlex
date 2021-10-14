from flask import current_app

from app.model.groups import Groups

def create_groups(data):

    new_data = Groups(**data)

    session = current_app.db.session
    session.add(new_data)
    session.commit()
    
    return {
        "cod":new_data.cod,
        "name":new_data.name
    }