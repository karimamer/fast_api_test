from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class CoffeeShop(BaseModel):
    name: str
    location: str
    rating: float 
    note: str = None

@app.get("/")
async def health_check():
    return {"message":  "The service is alive "}


@app.post("/coffee/")
async def create_coffeeshop(coffee: CoffeeShop):
    coffee_dict = coffee.dict()
    if coffee_dict.rating < 3:
        return coffee
    else:
        coffee_dict.update({"note": "I don't know about this place fam"})
        return coffee_dict

@app.get("/coffee/")
async def read_coffeshops(q: str = Query(
        None,
        title="Query string",
        description="Query string to get coffee shop",
        min_length=3,
    )):
    results = {"coffe shop": [{"name": "Foo"}, {"name": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



@app.get("/coffee/{shop_id}")
async def get_coffeeShop(shop_id:int, coffee_shop: CoffeeShop):
    results = {"coffe shop": coffee_shop.shop_id}

    return results
