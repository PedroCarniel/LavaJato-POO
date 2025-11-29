from abc import ABC, abstractmethod
from src.models.veiculo import Veiculo
from src.patterns.strategy import EstrategiaLavagem
from src.utils.validators import ValidadorVeiculo

# Contexto para passar dados entre os elos da corrente
class ContextoAtendimento:
    def __init__(self, veiculo: Veiculo, estrategia: EstrategiaLavagem):
        self.veiculo = veiculo
        self.estrategia = estrategia
        self.log_execucao = []
        self.preco_final = 0.0

class Handler(ABC):
    """Classe abstrata do elo da corrente."""
    def __init__(self):
        self._proximo = None

    def set_proximo(self, handler):
        self._proximo = handler
        return handler

    @abstractmethod
    def handle(self, contexto: ContextoAtendimento):
        if self._proximo:
            return self._proximo.handle(contexto)
        return context

# --- Elos da Corrente ---

class ValidacaoPlacaHandler(Handler):
    """Passo 1: Valida se a placa do veículo está correta."""
    def handle(self, ctx: ContextoAtendimento):
        if not ValidadorVeiculo.validar_placa(ctx.veiculo.placa):
            raise ValueError(f"Erro de Validação: A placa '{ctx.veiculo.placa}' é inválida.")
        
        ctx.log_execucao.append("✅ Placa validada com sucesso.")
        return super().handle(ctx)

class VerificacaoDisponibilidadeHandler(Handler):
    """Passo 2: Simula verificação de estoque/agenda."""
    def handle(self, ctx: ContextoAtendimento):
        # Aqui poderia haver consulta a banco de dados
        # Simulação: Carros muito antigos (ex: Modelo T) são rejeitados (exemplo lúdico)
        if "Ford T" in ctx.veiculo.modelo:
            raise Exception("Erro Operacional: Não temos peças para este modelo histórico.")
        
        ctx.log_execucao.append("✅ Disponibilidade e Estoque confirmados.")
        return super().handle(ctx)

class CalculoExecucaoHandler(Handler):
    """Passo 3: Executa a Estratégia e Calcula Preço."""
    def handle(self, ctx: ContextoAtendimento):
        # Executa o Strategy
        acao = ctx.estrategia.executar(ctx.veiculo)
        preco = ctx.estrategia.get_preco()

        # Aplica regra de negócio (Desconto Moto)
        if ctx.veiculo.get_tipo() == "Moto":
            preco *= 0.85
            ctx.log_execucao.append("ℹ️ Desconto de Moto aplicado (15%).")

        ctx.preco_final = preco
        ctx.log_execucao.append(f"🏁 Serviço Executado: {acao}")
        
        # Como é o último, retorna o contexto preenchido
        return ctx