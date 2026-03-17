# app/controllers/product_controllers.py

class ProductController:

    def __init__(self, service):
        self.service = service

    # POST
    def create_product(self, data):
        return self.service.create_data(data)  # already returns dict

    # GET
    def fetch_all_data(self):
        return self.service.get_the_whole_products()

    # DELETE
    def delete_product(self, name):
        return self.service.delete(name)

    # PATCH
    def update_product(self, name, data):
        return self.service.update(name, data)