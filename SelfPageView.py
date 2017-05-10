from flask import Blueprint, render_template
from dbModels import Item

view = Blueprint('SelfPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/self")
def whoami():
    items = Item.query.all()
    return render_template("SelfPage.html",
        posts = items
    )
