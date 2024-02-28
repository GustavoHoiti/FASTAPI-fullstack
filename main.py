from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from time import sleep
from models import Musicas
from models import musicas


def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(2)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(2)

app = FastAPI(
    title='API de Musicas',
    version='0.0.1',
    description='Uma API Fast'
)

@app.get('/musicas',
         description='Retorna todos as musicas disponíveis ou uma lista vazia.',
         summary='Retorna todos as musicas',
         response_model=List[Musicas],
         response_description='musicas encontradas com sucesso.')
async def musicas(db: Any = Depends(fake_db)):
    return musicas

@app.post('/musicas', status_code=status.HTTP_201_CREATED, response_model=Musicas)
async def post_musicas(musicas: Musicas):
    next_id: int = len(musicas) + 1
    musicas.id = next_id
    musicas.append(musicas)
    return musicas

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
