import uvicorn
from fastapi import FastAPI
from project.settings import settings
from decouple import config

app = FastAPI(
    debug=settings.DEBUG
)

if __name__ == '__main__':
    uvicorn.run(app, host=config("SERVER_HOST"), port=8000)

# uvicorn main:app --reload