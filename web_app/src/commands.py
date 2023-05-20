from src import db
from src.models.data_1 import Data_1
from src.models.data_2 import Data_2
from src.models.data_3 import Data_3

def create_db():
    """Creates database"""
    db.create_all()
    
def drop_db():
    """Cleans database"""
    db.drop_all()

def create_model_table():
    """Create table model in the database"""
    Data_1.__table__.create(db.engine)
    Data_2.__table__.create(db.engine)
    Data_3.__table__.create(db.engine)

def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, create_model_table]:
        app.cli.add_command(app.cli.command()(command))
