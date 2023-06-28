import requests
import pytest

def test_check_status_code():
    response = requests.get('https://pokemonbattle-stage.me:9101/trainers')
    assert  response.status_code == 200


def test_check_trainer_id():
    response = requests.get('https://pokemonbattle-stage.me:9101/trainers', 
                            params= {'trainer_id' : 1053})
    assert response.json()['trainer_name'] == 'Толян'