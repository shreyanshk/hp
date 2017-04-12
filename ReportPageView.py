from flask import Blueprint, render_template
import sqlite3

view = Blueprint('ReportPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/report")
def report():
    return render_template("ReportPage.html")
