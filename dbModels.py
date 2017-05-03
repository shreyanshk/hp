from Project import dbctx

class Item(dbctx.Model):
    __tablename__ = 'Items'
    id = dbctx.Column(dbctx.Integer, primary_key = True)
    obj = dbctx.Column(dbctx.String(30))
    objdesclng = dbctx.Column(dbctx.String(500))
    objdescsrt = dbctx.Column(dbctx.String(100))
    location = dbctx.Column(dbctx.String(50))
    imageext = dbctx.Column(dbctx.String(5))
    status = dbctx.Column(dbctx.String(10))

    def __init__(self, obj, objdescsrt, objdesclng, location, imageext, status = "Pending"):
        self.obj = obj
        self.objdescsrt = objdescsrt
        self.objdesclng = objdesclng
        self.location = location
        self.imageext = imageext
        self.status = status

    def __repr__(self):
        return "Item:\t{0}\nShortDesc:\n{1}\nLongDesc:\n{2}\nLocation:\t{3}\n".format(
            self.obj, self.objdescsrt, self.objdesclng, self.location,
            )

dbctx.create_all()
