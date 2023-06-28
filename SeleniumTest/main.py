import requests

token = 'cd8f6d9d331e1327ba32c6f14d7c1a9c'


add_pokemons_respons = requests.post('https://pokemonbattle-stage.me:9101/pokemons', 
              headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
                json = ({
      "name": "Жопля",
      "photo": "https://dolnikov.ru/pokemons/albums/196.png"}))
print(add_pokemons_respons.text)



change_pokemons_name = requests.put('https://pokemonbattle-stage.me:9101/pokemons', 
              headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
                json = ({
    "pokemon_id": "1052",
    "name": "Жопля",}))

print(change_pokemons_name.text)



catch_in_pokeball = requests.post('https://pokemonbattle-stage.me:9101/trainers/add_pokeball', 
              headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
                json = ({
    "pokemon_id": "1052"}))

print(catch_in_pokeball.text)