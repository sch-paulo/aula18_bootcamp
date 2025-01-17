import requests
from pydantic import BaseModel

# requests.get # select

# requests.post # create

# requests.put # update

# requests.delete # delete

# contrato de dados / schema de dados / view da minha API
class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int)   :
        
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return data['name'], types


###### PAREI 27:00