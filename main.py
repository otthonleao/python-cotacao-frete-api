from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Input com os dados do produto para o frete ser calculado
class Item(BaseModel):
	heightProduct: int
	widthProduct: int
	weightProduct: int

@app.post("/dados-produto")
def read_root(item: Item):
	return {
		"dimensao": {
						"altura": item.heightProduct,
						"largura": item.widthProduct
					},
		"peso": item.weightProduct
	}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q:Union[str, None] = None):
# 	return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id")
# def update_item(item_id: int, item: Item):
# 	return {"item_name": item.name, "item_id": item_id}