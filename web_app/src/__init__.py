from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database setup
db = SQLAlchemy()

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('src.config.Config')  # configure app using the Config class defined in src/config.py

    db.init_app(app) # initialise the database for the app

    with app.app_context():
        # from src import commands
        # commands.init_app(app) # initialise the app cli

        # from src.models.data_1 import Data_1
        # from src.models.data_2 import Data_2
        # from src.models.data_3 import Data_3
        # db.create_all()

        from src.endpoint_main.main import main_bp
        app.register_blueprint(main_bp)

        from src.endpoint_1.dt_1 import bp_data1
        app.register_blueprint(bp_data1)
        from src.endpoint_2.dt_2 import bp_data2
        app.register_blueprint(bp_data2)
        from src.endpoint_3.dt_3 import bp_data3
        app.register_blueprint(bp_data3)

        from src.endpoint_async.endp_async import bp_async
        app.register_blueprint(bp_async)

        return app
