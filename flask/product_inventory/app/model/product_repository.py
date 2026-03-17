# app/model/product_repository.py

class InMemoryRepo:
    def __init__(self):
        self._store = {}
        self._deleted_store = {}
        self._id_counter = 1

    # CREATE
    def insert_data(self, product):
        product_id = self._id_counter
        self._store[product_id] = product
        self._id_counter += 1
        return {"id": product_id, **product.to_dict()}

    # READ all
    def fetch_the_whole_catalogue(self):
        return [
            {"id": pid, **product.to_dict()}
            for pid, product in self._store.items()
        ]

    # GET product ID by name
    def get_id_by_name(self, name):
        for pid, product in self._store.items():
            if product.name == name:
                return pid
        return None

    # DELETE by name
    def delete_product_by_name(self, name):
        product_id = self.get_id_by_name(name)
        if product_id is None:
            raise KeyError(f"Product '{name}' not found")
        deleted_product = self._store.pop(product_id)
        self._deleted_store[product_id] = deleted_product
        return True

    # UPDATE by name (PATCH)
    def update_product_by_name(self, name, updated_fields):
        product_id = self.get_id_by_name(name)
        if product_id is None:
            raise KeyError(f"Product '{name}' not found")

        product = self._store[product_id]
        for key, value in updated_fields.items():
            if hasattr(product, key):
                setattr(product, key, value)
        self._store[product_id] = product
        return {"id": product_id, **product.to_dict()}