
from flask import Flask
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    # Allow only specific origins to access the app
    CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"], "allow_headers": ["Content-Type", "Authorization"]}})
    app.config.from_object('config.Config')

    # Import and register the blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app