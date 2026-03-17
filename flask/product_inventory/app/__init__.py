from flask import Flask

# import correct classes
from app.model.product_repository import InMemoryRepo
from app.service.product_services import ProductServiceLayer
from app.controllers.product_controllers import ProductController
from app.routing.product_routes import create_routes

def create_app():
    # instantiate the Flask app
    MKG = Flask(__name__)

    # MVC architecture
    repo = InMemoryRepo()                  # correct class name
    service = ProductServiceLayer(repo)    # business logic
    controllers = ProductController(service)
    product_routes = create_routes(controllers)

    # register routes
    MKG.register_blueprint(product_routes)

    return MKG

