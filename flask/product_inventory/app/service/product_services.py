from app.model.products_domain import Product

class ProductServiceLayer:

    def __init__(self, repo):   # rename parameter to be clear
        self.repo = repo

    def get_the_whole_products(self):
        # call the correct method in the repository
        return self.repo.fetch_the_whole_catalogue()
    
    def delete(self, id):
        self.repo.delete_a_product(id)

    def create_data(self, data):
        product_instance = Product(**data)
        return self.repo.insert_data(product_instance)