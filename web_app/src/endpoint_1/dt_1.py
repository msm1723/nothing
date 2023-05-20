from flask import Blueprint, jsonify
from src.models.data_1 import Data_1

bp_data1 = Blueprint('data1', __name__)

# just return data from table using ORM model capabilities
@bp_data1.route('/data1')
def data1():
    etities = Data_1.get_entities()
    return jsonify(etities)
