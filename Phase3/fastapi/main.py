from fastapi import FastAPI, Path

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

@app.get("/get-itemdd/{item_id}")
def get_item(item_id: int = Path(description="The Id of what you would like to view",title="THE ID",lt=3,gt=0)):
    if not item_id < 1 or item_id > 2:
        return inventory[item_id]
    
