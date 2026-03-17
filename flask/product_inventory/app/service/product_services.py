# app/service/product_services.py

from app.model.products_domain import Product

class ProductServiceLayer:

    def __init__(self, repo):
        self.repo = repo

    # GET all products
    def get_the_whole_products(self):
        return self.repo.fetch_the_whole_catalogue()

    # CREATE product
    def create_data(self, data):
        product_instance = Product(**data)
        return self.repo.insert_data(product_instance)

    # DELETE product by name
    def delete(self, name):
        return self.repo.delete_product_by_name(name)

    # UPDATE product by name (PATCH)
    def update(self, name, data):
        return self.repo.update_product_by_name(name, data)