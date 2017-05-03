from flask import Blueprint, render_template, request
from Project import dbctx
from dbModels import Item

view = Blueprint('ReportPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/report", methods = ["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("ReportPage.html")
    elif request.method == "POST":
        f = request.form
        print(f)
