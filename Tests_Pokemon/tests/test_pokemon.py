import requests
import pytest

# проверим, что статус код ответа - 200
def test_check_status_code():
 response = requests.get('https://pokemonbattle.me:9104/trainers')
 assert response.status_code == 200

# проверим, что имя тренера - Bishop
def test_part_of_response():
 response = requests.get('https://pokemonbattle.me:9104/trainers',
 params = {'trainer_id' : 3488})
 assert response.json()['trainer_name'] == 'Bishop'
