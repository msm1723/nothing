from flask import Blueprint, jsonify
from src.models.data_3 import Data_3

bp_data3 = Blueprint('data3', __name__)

@bp_data3.route('/data3')
def data3():
    etities = Data_3.get_entities()
    return jsonify(etities)
