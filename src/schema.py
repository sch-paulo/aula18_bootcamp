'''View: representação de como os dados vão vir da API'''

from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True