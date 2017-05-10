from flask import Flask
from flask import Blueprint
from dbModels import dbctx
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = "static/userimgs"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite3'
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    dbctx.init_app(app)

    from ReportPageView import view as ReportPage
    app.register_blueprint(ReportPage)

    from ReviewPageView import view as ReviewPage
    app.register_blueprint(ReviewPage)

    from SelfPageView import view as SelfPage
    app.register_blueprint(SelfPage)

    from WelcomePageView import view as WelcomePage
    app.register_blueprint(WelcomePage)

    with app.app_context():
        dbctx.create_all()
    return app
