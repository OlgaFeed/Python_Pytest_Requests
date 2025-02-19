import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '99b8e95abaa7b436114cf733251c1db6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "nnn",
    "photo_id": 694
}

'''response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create )
print(response.text)'''


body_name = {
    "pokemon_id": "239781",
    "name": "New Name",
    "photo_id": 2
}

'''response = requests.patch(url = f'{URL}/pokemons' , headers = HEADER, json = body_name )
print(response.text)'''

body_pokebal ={
    "pokemon_id": "239781"
}

response_pokebal = requests.post(url= f'{URL}/trainers/add_pokeball' , headers= HEADER, json= body_pokebal) 
print(response_pokebal.text)


