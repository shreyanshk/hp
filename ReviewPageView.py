from flask import Blueprint, render_template
import sqlite3

view = Blueprint('ReviewPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/review")
def review():
    return render_template("ReviewPage.html")
