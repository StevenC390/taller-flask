from flask import Blueprint, request
providers= Blueprint("providers",
                    __name__,
                    url_prefix="/api/v1/providers")
@providers.get("/")
def read_all():
    return "Reading al proveedor ... soon"

@providers.get("/<int:id>")
def read_one(id):
    return "Reading a proveedor ... soon"

@providers.post("/")
def create():
    return "Creating a proveedor ... soon"

@providers.put('/<int:id>')
@providers.patch('/<int:id>')
def update(id):
    return "Updating a proveedor ... soon"

@providers.delete("/<int:id>")
def delete(id):
    return "Removing a proveedor ... soon"

@providers.get("/<int:id>/products")
def read_one_libros(id):
    return "Reading a proveedor ... soon"