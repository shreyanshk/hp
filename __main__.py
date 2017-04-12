from flask import Flask
from flask import Blueprint

app = Flask(__name__)

from ReportPageView import view as ReportPage
app.register_blueprint(ReportPage)

from ReviewPageView import view as ReviewPage
app.register_blueprint(ReviewPage)

from SelfPageView import view as SelfPage
app.register_blueprint(SelfPage)

from WelcomePageView import view as WelcomePage
app.register_blueprint(WelcomePage)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.jinja_env.auto_reload = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(host='0.0.0.0', debug=True)
