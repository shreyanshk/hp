from flask import Blueprint, render_template

view = Blueprint('ReviewPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/review")
def review():
    from Project import dbctx
    from dbModels import Item
    items = Item.query.all()
    return render_template("ReviewPage.html",
        posts = items
    )
