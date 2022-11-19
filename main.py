from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Input com os dados do produto para o frete ser calculado
class Item(BaseModel):
	heightProduct: float
	widthProduct: float
	weightProduct: float

	# validate_input_ninja(item)

	# return {
	# 	"dimensao": {
	# 					"altura": item.heightProduct,
	# 					"largura": item.widthProduct
	# 				},
	# 	"peso": item.weightProduct
	# }

@app.post("/dados-produto")
def read_root(item: Item):
	ninja = validate_input_ninja(item)
	kabum = validate_input_kabum(item)
	lista = []
	if (ninja is not False):
		lista.append(ninja)
	if (kabum is not False):
		lista.append(kabum)
	return lista

# Validação para entrega Ninja
class ValidacaoNinja(BaseModel):
	constCalculoFrete: float = 0.3
	alturaMinima: float = 10.0
	alturaMaxima: float = 200.0
	larguraMinima: float = 6.0
	larguraMaxima: float = 140.0
	prazoEntrega: float = 6.0

def validate_input_ninja(item: Item):
	print(type(ValidacaoNinja().constCalculoFrete))
	if((item.heightProduct >= ValidacaoNinja().alturaMinima and item.heightProduct <= ValidacaoNinja().alturaMaxima)
	and (item.widthProduct >= ValidacaoNinja().larguraMinima and item.widthProduct <= ValidacaoNinja().larguraMaxima)):
		return {
			"nome": "Entrega Ninja",
			"valor_frete": (item.weightProduct * ValidacaoNinja().constCalculoFrete) / 10.0, #(peso * frete) / 10
			"prazo_dias": ValidacaoNinja().prazoEntrega
		}
	else:
		return False

# Validação para entrega Kabum
class ValidacaoKabum(BaseModel):
	constCalculoFrete: float = 0.2
	alturaMinima: float = 5.0
	alturaMaxima: float = 140.0
	larguraMinima: float = 13.0
	larguraMaxima: float = 125.0
	prazoEntrega: float = 4.0

def validate_input_kabum(item: Item):
	if((item.heightProduct >= ValidacaoKabum().alturaMinima) and (item.heightProduct <= ValidacaoKabum().alturaMaxima)
	and (item.widthProduct >= ValidacaoKabum().larguraMinima) and (item.widthProduct <= ValidacaoKabum().larguraMaxima)):
		return {
			"nome": "Entrega Kabum",
			"valor_frete": (item.weightProduct * ValidacaoKabum().constCalculoFrete) / 10.0,
			"prazo_dias": ValidacaoKabum().prazoEntrega
		}
	else:
		return False

# @app.post("/dados-produto/return")
