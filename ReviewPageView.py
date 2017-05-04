from flask import Blueprint, render_template
from Project import dbctx
from dbModels import Item

view = Blueprint('ReviewPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/review")
def review():
    items = Item.query.all()
    return render_template("ReviewPage.html",
        posts = items
    )
