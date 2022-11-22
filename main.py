from fastapi import FastAPI
from pydantic import BaseModel

import customShipping
import alternativeShipping
import inputProduct

app = FastAPI()

@app.post("/shipping")
def read_root(item: inputProduct.Item):
	alternative = alternativeShipping.validate_input_alternative(item)
	custom = customShipping.validate_input_custom(item)
	lista = []
	if (alternative is not False):
		lista.append(alternative)
	if (custom is not False):
		lista.append(custom)
	return lista


	# validate_input_ninja(item)

	# return {
	# 	"dimensao": {
	# 					"altura": item.heightProduct,
	# 					"largura": item.widthProduct
	# 				},
	# 	"peso": item.weightProduct
	# }