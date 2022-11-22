from pydantic import BaseModel

import inputProduct

class ValidateAlternativeShipping(BaseModel):
	constCalculoFrete: float = 0.3
	alturaMinima: float = 10.0
	alturaMaxima: float = 200.0
	larguraMinima: float = 6.0
	larguraMaxima: float = 140.0
	prazoEntrega: float = 6.0

def validate_input_alternative(item: inputProduct.Item):
	if((ValidateAlternativeShipping().alturaMinima >= item.heightProduct <= ValidateAlternativeShipping().alturaMaxima)
	and (ValidateAlternativeShipping().larguraMinima >= item.widthProduct <= ValidateAlternativeShipping().larguraMaxima)):
		return {
			"nome": "Entrega Ninja",
			"valor_frete": (item.weightProduct * ValidateAlternativeShipping().constCalculoFrete) / 10.0, #(peso * frete) / 10
			"prazo_dias": ValidateAlternativeShipping().prazoEntrega
		}
	else:
		return False