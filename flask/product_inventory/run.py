from app import create_app
from flask import Flask

# Create the app
app = create_app()

# Optional: simple root route to avoid 404 on '/'
@app.route("/")
def home():
    return "Flask Product Inventory Server is running!"

if __name__ == "__main__":
    # Run on port 5001, debug mode on
    app.run(port=5001, debug=True)