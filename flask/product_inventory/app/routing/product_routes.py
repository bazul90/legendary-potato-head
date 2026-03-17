# app/routing/product_routes.py

from flask import Blueprint, request, jsonify

product_routes_blueprint = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)

def create_routes(controllers):

    # GET all products
    @product_routes_blueprint.route("/", methods=["GET"])
    def fetch():
        products = controllers.fetch_all_data()
        return jsonify(products), 200

    # POST a new product
    @product_routes_blueprint.route("/", methods=["POST"])
    def create_a_record():
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 415

        payload = request.get_json()
        print(f"Received POST payload: {payload}")

        # Validate required fields
        required_fields = ["name", "price", "weight", "color", "durability"]
        missing = [f for f in required_fields if f not in payload]
        if missing:
            return jsonify({"error": f"Missing fields: {missing}"}), 400

        product = controllers.create_product(payload)
        return jsonify(product), 201

    # DELETE a product by name
    @product_routes_blueprint.route("/<string:name>", methods=["DELETE"])
    def delete_a_product(name):
        try:
            controllers.delete_product(name)
            return jsonify({"message": f"Product '{name}' deleted successfully"}), 200
        except KeyError:
            return jsonify({"error": f"Product '{name}' not found"}), 404

    # PATCH a product by name
    @product_routes_blueprint.route("/<string:name>", methods=["PATCH"])
    def patch_product(name):
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 415

        payload = request.get_json()
        print(f"Received PATCH payload for {name}: {payload}")

        try:
            updated_product = controllers.update_product(name, payload)
            return jsonify(updated_product), 200
        except KeyError:
            return jsonify({"error": f"Product '{name}' not found"}), 404

    return product_routes_blueprint