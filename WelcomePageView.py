from flask import Blueprint, render_template, redirect, url_for
import sqlite3

view = Blueprint('WelcomePageView',
        __name__,
        template_folder='templates',
        )

@view.route("/")
def whoami():
    return redirect(url_for("ReviewPageView.review"))
