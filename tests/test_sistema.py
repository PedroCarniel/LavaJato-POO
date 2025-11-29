import unittest
from src.models.veiculo import Carro, Moto
from src.patterns.strategy import LavagemSimples
from src.core.manager import LavaJatoManager

class TestLavaJato(unittest.TestCase):
    
    def setUp(self):
        # Reinicia o Singleton antes de cada teste para garantir isolamento
        LavaJatoManager._instancia = None
        self.manager = LavaJatoManager()

    def test_singleton_unico(self):
        m2 = LavaJatoManager()
        self.assertEqual(self.manager, m2, "O gerenciador deve ser a mesma instância (Singleton)")

    def test_calculo_preco_carro(self):
        carro = Carro("Fusca", "ABC-123", "Joao")
        estrategia = LavagemSimples() # Preço base 35.00
        
        self.manager.registrar_atendimento(carro, estrategia)
        saldo = self.manager.exibir_caixa()['saldo_atual']
        self.assertEqual(saldo, 35.00)

    def test_calculo_desconto_moto(self):
        moto = Moto("CB 500", "XYZ-999", "Maria")
        estrategia = LavagemSimples() # Preço base 35.00 -> Com desc 15% = 29.75
        
        self.manager.registrar_atendimento(moto, estrategia)
        saldo = self.manager.exibir_caixa()['saldo_atual']
        self.assertEqual(saldo, 29.75)

if __name__ == '__main__':
    unittest.main()