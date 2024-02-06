from pydantic import BaseModel

class Item(BaseModel):
	heightProduct: float
	widthProduct: float
	weightProduct: float
