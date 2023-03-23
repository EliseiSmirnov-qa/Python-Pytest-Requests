import requests

token = '4825a968bce0ef3e8cf96ab2926dc1f7'  # токен авторизации в системе

# создадим покемона
create_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons',
 headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
  json = {"name" : "Bluestar", "photo" : "https://dolnikov.ru/pokemons/albums/003.png"})
print(create_pokemon_response.text)

pokemon = create_pokemon_response.json()['id']  # id созданного покемона присваиваем переменную 

# сменим имя этого покемона
rename_pokemon_response = requests.put('https://pokemonbattle.me:9104/pokemons',
 headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
  json = {"pokemon_id": pokemon, "name" : "Pinkstar", "photo" : "https://dolnikov.ru/pokemons/albums/003.png"})
print(rename_pokemon_response.text)

# поймаем этого покемона в покебол
catch_pokemon_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
 headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
  json = {"pokemon_id": pokemon})
print(catch_pokemon_response.text)