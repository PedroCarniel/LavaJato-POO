from abc import ABC, abstractmethod

class Veiculo(ABC):
    """Classe base abstrata para todos os veículos."""
    def __init__(self, modelo: str, placa: str, dono: str):
        self._modelo = modelo
        self._placa = placa
        self._dono = dono # Novo atributo para robustez

    @property
    def placa(self):
        return self._placa

    @property
    def modelo(self):
        return self._modelo
    
    @property
    def dono(self):
        return self._dono

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    def __str__(self):
        return f"{self.get_tipo()}: {self._modelo} ({self._placa}) - Dono: {self._dono}"

class Carro(Veiculo):
    def get_tipo(self) -> str:
        return "Carro"

class Moto(Veiculo):
    def get_tipo(self) -> str:
        return "Moto"