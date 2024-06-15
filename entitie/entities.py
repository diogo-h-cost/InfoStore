from configs.config import db

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod = db.Column(db.String(50))
    desc = db.Column(db.String(80))
    uni = db.Column(db.Integer)

    def __init__(self, prod, desc, uni):
        self.prod = prod
        self.desc = desc
        self.uni = uni