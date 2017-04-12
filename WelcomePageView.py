from flask import Blueprint, render_template
import sqlite3

view = Blueprint('WelcomePageView',
        __name__,
        template_folder='templates',
        )

@view.route("/")
def whoami():
    return render_template("WelcomePage.html")
