import pytest
import json
from .data.data_dicts import data1_dict, data2_dict, data3_dict


def test_check_endpoint1(apply_test_data, api):
    data = api.endpoint1.get_data().json()
    expected = [{'entity_id': k, 'name': v} for k, v in data1_dict.items()]
    assert data == expected, 'Incorectd data on endpoint'

def test_check_endpoint2(apply_test_data, api):
    data = api.endpoint2.get_data().json()
    expected = [{'entity_id': k, 'name': v} for k, v in data2_dict.items()]
    assert data == expected, 'Incorectd data on endpoint'

def test_check_endpoint3(apply_test_data, api):
    data = api.endpoint3.get_data().json()
    expected = [{'entity_id': k, 'name': v} for k, v in data3_dict.items()]
    assert data == expected, 'Incorectd data on endpoint'

def test_check_endpoint_async(apply_test_data, api):
    data = api.endpoint_async.get_data().json()
    all_endpoints_dict =  sorted(data1_dict.items() | data2_dict.items() | data3_dict.items())
    expected = {str(k): v for k, v in all_endpoints_dict}
    assert data == expected, 'Incorectd data on endpoint'
