import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e845b7c96c87f8e06a4dd1f7470fd345'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
trainer_id = '7621'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200