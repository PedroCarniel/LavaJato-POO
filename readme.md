<img width="919" height="857" alt="image" src="https://github.com/user-attachments/assets/8f200905-b66a-498f-be84-ff34c661a5b8" /># 🚗 Sistema de Gestão de Lava Jato (Enterprise Edition)

Este projeto consiste em um sistema robusto desenvolvido em **Python** para o gerenciamento de um Lava Jato. O objetivo principal é demonstrar a aplicação prática e avançada dos **4 Pilares da Programação Orientada a Objetos (POO)** e a implementação de múltiplos **Padrões de Projeto (Design Patterns)**.

O sistema simula um fluxo de atendimento real: desde a validação da placa (via Regex) e verificação de disponibilidade, até a escolha da estratégia de lavagem, cálculo de preços e persistência de dados financeiros.

---

## 📋 Funcionalidades do Sistema

O sistema oferece um conjunto completo de ferramentas para a gestão operacional e financeira do Lava Jato:

* **Gestão de Atendimentos:** Cadastro de veículos (Carro/Moto) com **validação automática de placas** (Padrão Brasil e Mercosul via Regex).
* **Precificação Inteligente:** Cálculo automático de valores baseados no tipo de veículo, aplicando **regras de desconto dinâmicas** (ex: 15% off para motos).
* **Múltiplas Estratégias:** Seleção flexível de serviços de lavagem (Simples, Completa, Ecológica) utilizando o padrão *Strategy*.
* **Controle Financeiro:** Monitoramento centralizado do fluxo de caixa (via *Singleton*) e consulta interativa de **tabela de preços**.
* **Relatórios e Persistência:** Geração de logs detalhados de execução e **exportação de dados em JSON** para backup e auditoria.

## 📚 Descrição das Classes e Pilares da POO

O sistema foi modelado respeitando estritamente os pilares da orientação a objetos, dividindo responsabilidades em camadas específicas:

### 1. `Veiculo` (Abstração e Herança)
- **Localização:** `src/models/veiculo.py`
- **Descrição:** Classe base abstrata que define o contrato para qualquer veículo do sistema.
- **Pilar da POO:**
    - **Abstração:** Esconde a complexidade de dados genéricos, forçando as subclasses a implementarem métodos específicos.
    - **Herança:** Serve de classe "mãe" para `Carro` e `Moto`, centralizando atributos comuns (como placa, modelo e dono) e evitando repetição de código.

### 2. `LavaJatoManager` (Encapsulamento)
- **Localização:** `src/core/manager.py`
- **Descrição:** O núcleo do sistema. Gerencia o caixa financeiro, o histórico de logs e a orquestração do atendimento.
- **Pilar da POO:**
    - **Encapsulamento:** Os atributos críticos como `_saldo` e `_historico` são protegidos (private/protected). O acesso externo é restrito a métodos públicos, garantindo a segurança e integridade dos dados financeiros.

### 3. `EstrategiaLavagem` (Polimorfismo)
- **Localização:** `src/patterns/strategy.py`
- **Descrição:** Interface que padroniza os algoritmos de lavagem.
- **Pilar da POO:**
    - **Polimorfismo:** O método `executar()` assume comportamentos diferentes dependendo do objeto instanciado (`LavagemSimples`, `LavagemCompleta` ou `LavagemEcologica`). O sistema trata todas as estratégias de forma genérica, mas a execução real varia conforme a escolha do cliente.

### 4. `Handler` (Abstração e Delegação)
- **Localização:** `src/patterns/chain.py`
- **Descrição:** Classe abstrata que define a estrutura para a cadeia de validação (pipeline), permitindo que verificações sejam encadeadas sequencialmente.

---

## 🧩 Padrões de Projeto Aplicados

O sistema implementa **três padrões comportamentais/criacionais** principais solicitados, além de um estrutural adicional para robustez:

### 1. Factory Method (Criação)
- **Arquivo:** `src/patterns/factory.py` (Classe `VeiculoFactory`)
- **Objetivo:** Centraliza a lógica de criação de objetos.
- **Aplicação:** O cliente (`main.py`) solicita a criação de um veículo passando apenas o tipo ("1" para Carro, "2" para Moto), sem precisar conhecer as classes concretas ou suas importações, reduzindo o acoplamento do código.

### 2. Strategy Pattern (Comportamental)
- **Arquivo:** `src/patterns/strategy.py`
- **Objetivo:** Permite trocar o algoritmo (estratégia) de lavagem em tempo de execução.
- **Aplicação:** O usuário escolhe entre Lavagem Simples, Completa ou Ecológica. Cada classe encapsula seu próprio preço e mensagem de log. Isso facilita a manutenção e a adição de novos serviços no futuro sem quebrar o código existente.

### 3. Chain of Responsibility (Comportamental)
- **Arquivo:** `src/patterns/chain.py`
- **Objetivo:** Cria um pipeline de processamento onde cada etapa decide se passa o pedido adiante ou encerra com erro.
- **Aplicação:** Ao registrar um atendimento, o sistema segue o fluxo:
    1.  **ValidacaoPlacaHandler:** Usa Regex para validar se a placa segue o padrão Brasileiro ou Mercosul.
    2.  **VerificacaoDisponibilidadeHandler:** Checa regras de negócio (ex: restrição de modelos antigos).
    3.  **CalculoExecucaoHandler:** Se todas as etapas anteriores passarem, executa a lavagem e cobra.

### 4. Singleton (Estrutural) - *Padrão Extra*
- **Arquivo:** `src/core/manager.py`
- **Objetivo:** Garante que exista apenas uma instância da classe gerenciadora.
- **Aplicação:** Assegura que todo o sistema compartilhe o mesmo "Caixa Financeiro". Se tentarmos instanciar o `LavaJatoManager` em dois lugares diferentes, ambos apontarão para o mesmo objeto na memória.

## 5. 📐 Diagrama de Classes (UML)

O diagrama abaixo ilustra a arquitetura modular do sistema, detalhando a aplicação dos padrões de projeto e as relações entre as classes.

<img width="919" height="857" alt="image" src="https://github.com/user-attachments/assets/fb7caf08-868a-4cc6-8f6e-a9872b9e0b2d" />


---

## 🚀 Instruções de Execução e Testes

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPO.git](https://github.com/SEU-USUARIO/SEU-REPO.git)
    cd SEU-REPO
    ```

2.  **Verifique a Estrutura:**
    O projeto deve conter as pastas `src/` (com `models`, `patterns`, `core`, `utils`) e `tests/`.

3.  **Executar o Sistema:**
    No terminal, na raiz do projeto, execute:
    ```bash
    python main.py
    ```
    *Siga as instruções do menu interativo para cadastrar veículos e realizar lavagens.*

4.  **Executar Testes Unitários:**
    Para validar a lógica do sistema e a integridade dos padrões implementados:
    ```bash
    python -m unittest discover tests
    ```

---
**Autor:** Pedro Henrique Castaman Carniel

**Disciplina:** Tecnologia Orientada a Objetos (TOO)
