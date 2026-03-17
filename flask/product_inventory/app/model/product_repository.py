# ==========================================
# IN-MEMORY REPOSITORY (SIMULATED DATABASE)
# ==========================================
# This class acts like a simple database.
# Instead of using a real database like PostgreSQL,
# all data is stored in Python dictionaries in memory.

class InMemoryRepo:
    def __init__(self):
        # Two dictionaries are initialized here:
        # - _store holds all active products
        # - _deleted_store keeps deleted products for possible restoration
        self._store = {}
        self._deleted_store = {}

        # This counter ensures every product gets a unique ID.
        # It prevents duplication issues when items are deleted.
        self._id_counter = 1

    def insert_data(self, product):
        # CREATE operation:
        # A unique ID is generated for each new product,
        # then the product is stored in the main dictionary.

        product_id = self._id_counter
        self._store[product_id] = product

        # The counter is incremented so the next product gets a new ID.
        self._id_counter += 1

        # The stored product is returned along with its ID,
        # similar to how real APIs respond.
        return {"id": product_id, **product.to_dict()}

    def fetch_a_single_product(self, product_id):
        # READ (single item):
        # .get() is used to safely fetch the product.
        # This avoids errors if the product does not exist.

        product = self._store.get(product_id)

        if product:
            # If found, return the product with its ID.
            return {"id": product_id, **product.to_dict()}

        # If not found, return None instead of crashing.
        return None

    def fetch_the_whole_catalogue(self):
        # READ (all items):
        # Returns a list of all products in the system.
        # Each product is formatted to include its ID.

        return [
            {"id": product_id, **product.to_dict()}
            for product_id, product in self._store.items()
        ]

    def update_a_product(self, product_id, updated_product):
        # UPDATE operation:
        # First checks if the product exists.
        # If it does, the old product is replaced with the updated one.

        if product_id in self._store:
            self._store[product_id] = updated_product

            # The updated product is returned.
            return {"id": product_id, **updated_product.to_dict()}

        # If the product does not exist, return None.
        return None

    def delete_a_product(self, product_id):
        # DELETE operation (soft delete):
        # The product is removed from the main store,
        # but saved in a separate dictionary instead of being permanently deleted.

        if product_id in self._store:
            deleted_product = self._store.pop(product_id)

            # Store the deleted product for possible restoration.
            self._deleted_store[product_id] = deleted_product
            return True

        # If the product does not exist, return False.
        return False

    def restore_deleted_product(self, product_id):
        # RESTORE operation:
        # Checks if the product exists in the deleted store.
        # If found, it is moved back to the main store.

        if product_id in self._deleted_store:
            product = self._deleted_store.pop(product_id)
            self._store[product_id] = product

            # Return the restored product.
            return {"id": product_id, **product.to_dict()}

        # If not found, return None.
        return None