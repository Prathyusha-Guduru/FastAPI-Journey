from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	name : str
	price : float
	brand : Optional[str] = None

class UpdateItem(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None
    brand : Optional[str] = None

inventory = {
	1:{
		"name" : "milk", 
		"price" : 3.99, 
		"brand" : "vijaya"
	}
}



@app.get("/")
def home():
	return "Hello worald"
# Path parameters
@app.get("/get-item/{item_id}/{name}")
# type hint
def get_item(item_id: int = Path(None,description = "Unique Id of the item you would like to view")):
	return inventory[item_id] 

@app.get("/get-by-name/{item_id}")
def about(*,item_id:int,name : Optional[str] = None,test : int):
	for item_id in inventory:
		if inventory[item_id]["name"] == name:
			return inventory[item_id]
		else: 
			return "data not found"

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item : Item):
    if item_id in inventory:
        return {"Error":"Already exists"}
    else:
        inventory[item_id] = item
        return {"Created" : inventory[item_id]}



@app.put("/update-item/{item_id}")
def update_item(item_id:int,item : UpdateItem):
    if item_id not in inventory:
        return {"Error":"Does not exists"}
    else:
         
        if item.name !=None: 
            inventory[item_id]["name"] = item.name
        if item.price !=None:
            inventory[item_id]["price"] = item.price
        if item.brand !=None:
            inventory[item_id]["brand"] = item.brand
        return {"Updated" : inventory[item_id]}


@app.delete("/delete_item/{item_id}")
def delete_item(item_id:int):
    if item_id not in inventory:
        return {"Error":"Does not exists"}
    else:
        del inventory[item_id]
        return {"Deleted"}
    

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def root():
#     print("Hello")
#     return {"message": "Hello World"}


