from flask import Blueprint, request, jsonify

product_routes_blueprint = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)

def create_routes(controllers):

    @product_routes_blueprint.route("/", methods=["GET"])
    def fetch():
        return jsonify(controllers.fetch_all_data())

    @product_routes_blueprint.route("/", methods=["POST"])
    def create_a_record():
        payload = request.json
        print(f"this is the user data {payload}")
        user_input = controllers.create_product(payload)
        return jsonify(user_input), 201

    return product_routes_blueprint 