from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/userimgs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite3'
dbctx = SQLAlchemy(app)

from ReportPageView import view as ReportPage
app.register_blueprint(ReportPage)

from ReviewPageView import view as ReviewPage
app.register_blueprint(ReviewPage)

from SelfPageView import view as SelfPage
app.register_blueprint(SelfPage)

from WelcomePageView import view as WelcomePage
app.register_blueprint(WelcomePage)
