def init_app(app):
    from app.views.certification import bp as bp_certification
    from app.views.groups_view import bp as bp_groups

    app.register_blueprint(bp_certification)
    app.register_blueprint(bp_groups)