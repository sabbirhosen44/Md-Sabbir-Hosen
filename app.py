# Main entry point for the Travel Deal API.
import os
from flask import Flask
from dotenv import load_dotenv
from routes.deal_routes import deal_bp
from database.db import db
from utils.statistics import (
    increment_total_requests,
    increment_successful_requests,
    increment_failed_requests,
)

# Load Environment
load_dotenv()

# Initializes the Flask app
app = Flask(__name__)

# Configures environment variables,
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Sets up the database, and registers Blueprints.
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(deal_bp)


# Track total requests
@app.before_request
def before_request():
    increment_total_requests()


# Track success and failed requests
@app.after_request
def after_request(response):
    if response.status_code < 400:
        increment_successful_requests()
    else:
        increment_failed_requests()

    return response


# Health Status Check
@app.route("/")
def health():
    return {"success": True, "message": "Travel Deal Management API is running"}


if __name__ == "__main__":
    app.run(debug=True)
