from enum import Enum
from src.models.veiculo import Veiculo, Carro, Moto

class TipoVeiculo(Enum):
    CARRO = "1"
    MOTO = "2"

class VeiculoFactory:
    """Fábrica responsável por instanciar veículos."""
    
    @staticmethod
    def criar(tipo: str, modelo: str, placa: str, dono: str) -> Veiculo:
        if tipo == TipoVeiculo.CARRO.value:
            return Carro(modelo, placa, dono)
        elif tipo == TipoVeiculo.MOTO.value:
            return Moto(modelo, placa, dono)
        else:
            raise ValueError(f"Tipo de veículo '{tipo}' inválido.")