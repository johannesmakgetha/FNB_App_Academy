from fastapi import FastAPI, Path,Query

app = FastAPI()


inventory = {
    1 : {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    },
    2 : {
            "name": "Eggs",
            "price": 8.99,
            "brand": "Large"
        }

}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The Id of what you would like to view",title="THE ID",lt=3,gt=0)):
    if not item_id < 1 or item_id > 2:
        return inventory[item_id]
    

@app.get("/get-by-name")
def get_item(name:str = Query(description="The name of the item you want to view")):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}