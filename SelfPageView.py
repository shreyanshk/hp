from flask import Blueprint, render_template

view = Blueprint('SelfPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/self")
def whoami():
    from dbModels import Item
    items = Item.query.all()
    return render_template("SelfPage.html", posts = items)
