import json
import os
from datetime import datetime
from src.models.veiculo import Veiculo
from src.patterns.strategy import EstrategiaLavagem
from src.patterns.chain import (
    ContextoAtendimento, 
    ValidacaoPlacaHandler, 
    VerificacaoDisponibilidadeHandler, 
    CalculoExecucaoHandler
)

class LavaJatoManager:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(LavaJatoManager, cls).__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia

    def _inicializar(self):
        self._historico = []
        self._saldo = 0.0
        
        # Configurando a Chain of Responsibility (Pipeline)
        # Validação -> Disponibilidade -> Execução
        self._pipeline = ValidacaoPlacaHandler()
        self._pipeline.set_proximo(VerificacaoDisponibilidadeHandler())\
                      .set_proximo(CalculoExecucaoHandler())

    def processar_atendimento(self, veiculo: Veiculo, estrategia: EstrategiaLavagem):
        # Cria o pacote de dados (Contexto)
        contexto = ContextoAtendimento(veiculo, estrategia)
        
        try:
            # Dispara a cadeia de responsabilidade
            resultado_ctx = self._pipeline.handle(contexto)
            
            # Se não deu erro, atualiza o caixa (Singleton Logic)
            self._saldo += resultado_ctx.preco_final
            self._registrar_log(resultado_ctx)
            
            return {
                "status": "sucesso",
                "valor": resultado_ctx.preco_final,
                "logs": resultado_ctx.log_execucao
            }
            
        except Exception as e:
            # Se algum Handler levantar erro, capturamos aqui
            return {
                "status": "erro",
                "mensagem": str(e)
            }

    def _registrar_log(self, ctx: ContextoAtendimento):
        detalhe = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "veiculo": ctx.veiculo.placa,
            "servico": ctx.estrategia.get_nome(),
            "valor": round(ctx.preco_final, 2)
        }
        self._historico.append(detalhe)

    def exibir_caixa(self):
        return {
            "total_atendimentos": len(self._historico),
            "saldo_atual": round(self._saldo, 2)
        }

    def salvar_relatorio_json(self):
        caminho = "data/relatorios/relatorio_financeiro.json"
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump({"caixa": self.exibir_caixa(), "log": self._historico}, f, indent=4)
        return caminho