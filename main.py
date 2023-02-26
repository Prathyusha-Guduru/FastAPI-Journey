from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None



@app.get("/")
def read_root():
    print("hello worlds")
    print("reload check")
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

@app.get("/items/{item_id}")
def get_needy(item_id:int, needy:bool):
    return {"item_id":item_id, "needy":needy}

@app.put("/items/{item_id}")
def create_new_item(item_id:int, item:Item):
    return {"item_id":item_id, **item.dict()}

@app.post("/items/")
def create_item(item:Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return "njjefq"
    

# if __name__ == "__main__":
#     app.run("example:app", host="127.0.0.1",port="5000",reload=True )