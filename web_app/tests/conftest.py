import pytest

from src.models.data_1 import Data_1
from src.models.data_2 import Data_2
from src.models.data_3 import Data_3
from .data.data_dicts import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .api_wrappers.main import TestApplicationApi


@pytest.fixture(scope='session', autouse=True)
def apply_test_data():
    engine = create_engine('postgresql://barack_obama:qwe123QWE@127.0.0.1:5432/the_base')
    Session = sessionmaker(bind=engine)
    
    # Remove and recreate tables
    Data_1.metadata.drop_all(engine)
    Data_2.metadata.drop_all(engine)
    Data_3.metadata.drop_all(engine)

    Data_1.metadata.create_all(engine)
    Data_2.metadata.create_all(engine)
    Data_3.metadata.create_all(engine)

    # Populate tables with test data
    s = Session()
    for i, v in data1_dict.items():
        s.add(Data_1(i, v))
    for i, v in data2_dict.items():
        s.add(Data_2(i, v))
    for i, v in data3_dict.items():
        s.add(Data_3(i, v))
    s.commit()

@pytest.fixture
def api():
    # Let's pretend here I am logged into the application and passing the logged in api to the test
    yield TestApplicationApi()

