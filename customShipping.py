from pydantic import BaseModel

import inputProduct

class ValidateCustomShipping(BaseModel):
	constCalculoFrete: float = 0.2
	alturaMinima: float = 5.0
	alturaMaxima: float = 140.0
	larguraMinima: float = 13.0
	larguraMaxima: float = 125.0
	prazoEntrega: float = 4.0

def validate_input_custom(item: inputProduct.Item):
	if((ValidateCustomShipping().alturaMinima >= item.heightProduct <= ValidateCustomShipping().alturaMaxima)
	and (ValidateCustomShipping().larguraMinima >= item.widthProduct <= ValidateCustomShipping().larguraMaxima)):
		return {
			"nome": "Entrega Padrão",
			"valor_frete": (item.weightProduct * ValidateCustomShipping().constCalculoFrete) / 10.0,
			"prazo_dias": ValidateCustomShipping().prazoEntrega
		}
	else:
		return False