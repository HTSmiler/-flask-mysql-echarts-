from app.extensions import db

class PySJ(db.Model):
    __tablename__ = 'python_dw'
    f1 = db.Column(db.Integer, primary_key=True)
    BT= db.Column(db.String(255))
    JG = db.Column(db.String(255))
    ZZ = db.Column(db.String(255))
    CBSJ = db.Column(db.String(255))
    PLS = db.Column(db.String(255))