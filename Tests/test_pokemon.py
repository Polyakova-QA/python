import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '10e5521a13e5a90e2d9e27ad3eef1538'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}

def test_status_cod():
    responce = requests.get(url = f'{URL}/trainers', headers = HEADER)
    assert responce.status_code == 200

def test_name_tr():
    responce = requests.get(url = f'{URL}/trainers', headers = HEADER, params={'trainer_id':4854})
    assert responce.json()['data'][0]['id'] == '4854'

def test_name():
    responce = requests.get(url = f'{URL}/trainers', headers = HEADER, params={'trainer_id':4854})
    assert responce.json()['data'][0]["trainer_name"] == 'Идемпотент'