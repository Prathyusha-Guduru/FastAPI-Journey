from fastapi import FastAPI
from . import schema

app = FastAPI()

@app.post('/blog')
def create(request : schema.Blog):
    return request