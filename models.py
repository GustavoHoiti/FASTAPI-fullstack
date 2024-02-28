from typing import Optional
from pydantic import BaseModel, validator

class Musicas(BaseModel):
    id: Optional[int] = None
    banda: str
    nome_banda: str  
    album: str  

    @validator('descricao')
    def validar_descricao(cls, value: str):
        # Validacao 1
        palavras = value.split(' ')
        if len(palavras) < 4:
            print("A descrição deve ter pelo menos 4 palavras.")
            #raise ValueError('A descrição deve ter pelo menos 3 palavras.')
        # Validacao 2
        if value.islower():
            print("A descrição deve ser capitalizada")
            #raise ValueError('A descrição deve ser capitalizada.')
        return value
musicas = [
    Musicas(id=1, banda='I wanna be yours', nome_banda='Artic Monkeys', album='AM'),
    Musicas(id=2, banda='Do I Wanna Know?', nome_banda='Artic Monkeys', album='AM'),
]
