import re

class ValidadorVeiculo:
    @staticmethod
    def validar_placa(placa: str) -> bool:
        """
        Valida placas nos formatos:
        - Padrão Antigo: ABC-1234
        - Padrão Mercosul: ABC1D23
        """
        # Remove espaços e traços e deixa maiúsculo
        placa_limpa = placa.replace("-", "").upper().strip()
        
        # Regex para os dois padrões
        # [A-Z]{3} = 3 letras
        # [0-9] = 1 número
        # [0-9A-Z] = 1 número ou letra (diferença Mercosul)
        # [0-9]{2} = 2 números
        padrao = r"^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$"
        
        if re.match(padrao, placa_limpa):
            return True
        return False