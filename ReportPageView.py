from flask import Blueprint, render_template, request
from Project import dbctx
from dbModels import Item
import os

view = Blueprint('ReportPageView',
        __name__,
        template_folder='templates',
        )

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@view.route("/report", methods = ["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("ReportPage.html")
    elif request.method == "POST":
        f = request.form
        if 'image' not in request.files:
            return render_template("ReportPage.html", err = 0)
        else:
            i = request.files['image']
            if i.filename == '':
                return render_template("ReportPage.html", err = 1)
            if i and allowed_file(i.filename):
                ext = "." + i.filename.split(".")[1]
                item = Item(f['obj'], f['objdescsrt'], f['objdesclng'], f['location'], ext)
                dbctx.session.add(item)
                dbctx.session.commit()
                i.save(os.path.join('static/usrimgs', str(item.id))+ext)
                return render_template("ReportPage.html")
    return render_template("ReportPage.html")
