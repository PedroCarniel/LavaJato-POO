from abc import ABC, abstractmethod
from src.models.veiculo import Veiculo

class EstrategiaLavagem(ABC):
    """Interface Strategy."""
    @abstractmethod
    def executar(self, veiculo: Veiculo) -> str:
        pass

    @abstractmethod
    def get_preco(self) -> float:
        pass

    @abstractmethod
    def get_nome(self) -> str:
        pass

class LavagemSimples(EstrategiaLavagem):
    def executar(self, veiculo: Veiculo) -> str:
        return f"Lavagem com Água e Sabão neutro aplicada ao {veiculo.modelo}."

    def get_preco(self) -> float:
        return 35.00

    def get_nome(self) -> str:
        return "Simples"

class LavagemCompleta(EstrategiaLavagem):
    def executar(self, veiculo: Veiculo) -> str:
        return f"Lavagem Completa + Cera + Aspiração interna no {veiculo.modelo}."

    def get_preco(self) -> float:
        return 80.00
    
    def get_nome(self) -> str:
        return "Completa"

class LavagemEcologica(EstrategiaLavagem):
    def executar(self, veiculo: Veiculo) -> str:
        return f"Lavagem a Seco (Biodegradável) no {veiculo.modelo}."

    def get_preco(self) -> float:
        return 60.00
    
    def get_nome(self) -> str:
        return "Ecológica"