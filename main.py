import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '10e5521a13e5a90e2d9e27ad3eef1538'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
body_made_pokemon = {
    "name": "Докер Фэйс",
    "photo_id": 66
}
body_new_name = {
    "pokemon_id": "65127",
    "name": "Poker Face",
    "photo_id": 33
}
body_pull = {
    "pokemon_id": "65127"
}

'''responce = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_made_pokemon)
print(responce.text)'''

'''responce_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(responce_name.text)'''

'''responce_pull = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pull)
print(responce_pull.text)'''