from flask import Blueprint, render_template
import sqlite3

view = Blueprint('SelfPageView',
        __name__,
        template_folder='templates',
        )

@view.route("/self")
def whoami():
    posts = [
        {
            'obj' : "this is a test obj",
            'date' : "1/1/2016",
            'objdescsrt' : "this is a short desc",
            'location' : "mba ampli",
            'objdesclng' : "this is a long desc",
            'picname' : "picture.jpg"
        },
        {
            'obj' : "this is a test obj1",
            'date' : "1/1/20161",
            'objdescsrt' : "this is a short1 desc",
            'location' : "mba ampli1",
            'objdesclng' : "this is 1a long desc",
            'picname' : "picture.jpg"

        }
    ]
    return render_template("SelfPage.html", posts=posts)
