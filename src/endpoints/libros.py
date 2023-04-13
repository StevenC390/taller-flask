from flask import Blueprint
products = Blueprint("products",
                    __name__,
                    url_prefix="/api/v1/products")
@products.get("/")
def read_all():
    return "Reading the books ... soon"

@products.get("/<int:id>")
def read_one(id):
    return "Reading a book ... soon"

@products.post("/")
def create():
    return "Creating a book ... soon"

@products.put('/<int:id>')
@products.patch('/<int:id>')
def update(id):
    return "Updating a book ... soon"

@products.delete("/<int:id>")
def delete(id):
    return "Removing a book ... soon"