from datetime import datetime
from src.database import db, ma

class Product(db.model):
    code        = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement = True)
    name        = db.Column(db.String(50),unique=True,nullable=False)
    price       = db.Column(db.Float,nullable=False)
    expiration  = db.Column(db.DateTime,default=datetime.year(2025),nullable=True)
    created_at  = db.Column(db.DateTime,default=datetime.now())
    updated_at  = db.Column(db.DateTime,onupdate=datetime.now())
    user_id     = db.Column(db.String(10),db.ForeignKey('user.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    
    def __init__(self, **fields):
        super().__init_(**fields)
        
    def __repr__ (self) -> str:
        return f"Product >>> {self.name}"
    
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # fields =()
        model = Product
        iclude_fk = True
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)