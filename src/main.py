import routing
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from models import Character

app = FastAPI()


@app.get('/')
def main():
    return 'FireEmblemAPI - The Unofficial Fire Emblem API :)'


@app.get('/error')
def error():
    return 'Nothing to see here :('


@app.get('/games')
async def get_games():
    return routing.get_games()


@app.get('/{game}/character/{character}', response_model=Character)
async def get_character(game: str, character: str):
    return routing.get_character(game, character)


@app.get('/{game}/characters', response_model=list[Character])
async def get_characters(game: str):
    return routing.get_characters(game)


@app.get('/{game}/skills')
async def get_skills(game: str):
    return routing.get_skills(game)


@app.get('/{game}/base_growths/{character}')
async def get_base_growths_for_character(game: str, character: str):
    return routing.get_base_growths_for_character(game, character)


@app.get('/{game}/base_growths')
async def get_base_growths(game: str):
    return routing.get_base_growths(game)


@app.get('/{game}/meta')
async def get_meta(game: str):
    return routing.get_meta(game)


@app.exception_handler(StarletteHTTPException)
def custom_http_exception_handler(request, exc):
    return RedirectResponse('/error')
