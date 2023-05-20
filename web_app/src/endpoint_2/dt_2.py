from flask import Blueprint, jsonify
from src.models.data_2 import Data_2

bp_data2 = Blueprint('data2', __name__)

@bp_data2.route('/data2')
def data2():
    etities = Data_2.get_entities()
    return jsonify(etities)
