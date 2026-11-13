from fastapi import FastAPI, Path,Query
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: float 
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None 
    brand: Optional[str] = None


app = FastAPI()


inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The Id of what you would like to view",title="THE ID",gt=0)):
    if not item_id < 1 or item_id > 2:
        return inventory[item_id]
    

@app.get("/get-by-name")
def get_item(name:str = Query(description="The name of the item you want to view")):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.get("/all-items")
def all_items():
     return inventory


@app.post("/create-item/item_id")
def create_item(item_id: int,item:Item):
    if item_id in inventory:
        return {"Data" : "Data already exist"}
    inventory[item_id] = item
    return inventory[item_id]



@app.put("/update-item/{item_id}")
def update_item(*,item_id: int = Path(description="The Id of Item to update",gt=0), item: UpdateItem):
    if item_id not in inventory:
        return {"Data": "Id does not exist"}

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
            inventory[item_id].price = item.price

    if item.brand != None:
            inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item/")
def delete_item(item_id: int = Query(...,description="The Id of item to delete", gt=0)):
     if item_id not in inventory:
          return {"Data": "Item ID does not exist"}

     del inventory[item_id]
     return {"Deleted": "Item deleted"}