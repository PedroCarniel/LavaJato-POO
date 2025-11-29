import sys
from src.patterns.factory import VeiculoFactory
from src.patterns.strategy import LavagemSimples, LavagemCompleta, LavagemEcologica
from src.core.manager import LavaJatoManager

def exibir_tabela_precos():
    """
    Exibe uma tabela comparativa de preços.
    Instancia as estratégias apenas para ler seus preços base.
    """
    # Lista das estratégias disponíveis
    opcoes = [LavagemSimples(), LavagemCompleta(), LavagemEcologica()]
    
    print("\n" + "="*55)
    print(f"{'TIPO DE LAVAGEM':<20} | {'CARRO (R$)':<12} | {'MOTO (R$)*':<12}")
    print("="*55)
    
    for servico in opcoes:
        nome = servico.get_nome()
        preco_carro = servico.get_preco()
        # Simula o desconto de 15% que existe na regra de negócio (Chain)
        preco_moto = preco_carro * 0.85 
        
        print(f"{nome:<20} | R$ {preco_carro:<9.2f} | R$ {preco_moto:<9.2f}")
    
    print("-" * 55)
    print("* Motos possuem 15% de desconto aplicado automaticamente.")
    print("=" * 55 + "\n")

def main():
    sistema = LavaJatoManager()
    
    while True:
        print("\n=== LAVA JATO SYSTEM ENTERPRISE ===")
        print("1. Novo Atendimento")
        print("2. Consultar Caixa")
        print("3. Exportar JSON")
        print("4. Consultar Tabela de Preços") # Nova Opção
        print("0. Sair")
        
        op = input("Opção: ")

        if op == "1":
            print("\n--- Dados do Veículo ---")
            tipo = input("Tipo (1-Carro, 2-Moto): ")
            modelo = input("Modelo: ")
            placa = input("Placa (ABC-1234 ou Mercosul): ")
            dono = input("Dono: ")

            try:
                # Factory cria o veículo
                veiculo = VeiculoFactory.criar(tipo, modelo, placa, dono)
                
                print("\n--- Serviço ---")
                print("1. Simples | 2. Completa | 3. Ecológica")
                sel = input("Escolha: ")
                
                # Strategy define o algoritmo
                estrategia = LavagemSimples() # Default
                if sel == "2": estrategia = LavagemCompleta()
                elif sel == "3": estrategia = LavagemEcologica()

                # Manager dispara a Chain of Responsibility
                resultado = sistema.processar_atendimento(veiculo, estrategia)

                if resultado['status'] == 'sucesso':
                    print("\n✅ ATENDIMENTO REALIZADO!")
                    print(f"Valor final: R$ {resultado['valor']:.2f}")
                    print("Log Operacional:")
                    for log in resultado['logs']:
                        print(f"  -> {log}")
                else:
                    print(f"\n❌ ERRO NO PROCESSO: {resultado['mensagem']}")

            except ValueError as ve:
                print(f"Erro de entrada: {ve}")

        elif op == "2":
            cx = sistema.exibir_caixa()
            print(f"\n💰 Saldo: R${cx['saldo_atual']}")
            print(f"📈 Qtd Atendimentos: {cx['total_atendimentos']}")
        
        elif op == "3":
            path = sistema.salvar_relatorio_json()
            print(f"Arquivo salvo em: {path}")

        elif op == "4":
            exibir_tabela_precos()

        elif op == "0":
            sys.exit()
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()