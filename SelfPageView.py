from flask import Blueprint, render_template
import sqlite3

view = Blueprint('SelfPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/self")
def whoami():
    return render_template("SelfPage.html")
