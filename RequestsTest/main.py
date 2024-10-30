import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e845b7c96c87f8e06a4dd1f7470fd345'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "2Pac",
    "photo_id": 13
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "PDiddy",
    "photo_id": 2
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)