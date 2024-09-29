<<<<<<< HEAD
# Dbank1 - Versão 1.1
# Projeto de Sistema Bancário
### Descrição
Este é um projeto simples de sistema bancário feito com Python, onde o usuário realizar pode realizar operações como depósito, saque e visualização de extrato. Incluindo validações para garantir que os valores são válidos.

### Funcionalidades
* **Cadastro de usuários:** Cria novos usuários com informações pessoais e uma conta bancária inicial.
* **Gerenciamento de contas:** Permite criar novas contas para usuários existentes e realizar operações bancárias.
* **Operações financeiras:** Suporta depósitos e saques, com validações de limites e saldo.
* **Extrato bancário:** Exibe o histórico de transações de uma conta específica.

### Como Usar
1. **Executar o script:** Execute o script Python para iniciar o sistema.
2. **Seguir as instruções:** O sistema apresentará um menu com as opções disponíveis.
3. **Realizar operações:** Selecione a opção desejada e siga as instruções para realizar as operações.

### Estrutura do Código
* **`clientes`:** Lista de dicionários, onde cada dicionário representa um cliente com suas informações e contas.
* **Funções:**
    * `limpar_cpf`: Limpa e valida o CPF.
    * `gerar_numero_conta`: Gera um número de conta único.
    * `novo_usuario`: Cria um novo usuário e sua primeira conta.
    * `nova_conta`: Cria uma nova conta para um usuário existente.
    * `listar_contas`: Lista todas as contas de um usuário.
    * `selecionar_conta`: Permite ao usuário selecionar uma conta específica.
    * **Outras funções:** Realizam operações como depósito, saque, consulta de extrato, etc.

### Considerações
* **Limitações:** O sistema é uma demonstração e possui limitações, os dados são perdidos ao encerrar o programa.
* **Melhorias:** Para um sistema bancário real, seria necessário implementar funcionalidades adicionais como transferência entre contas, pagamento de contas, etc., além de garantir a segurança dos dados.


### Tecnologias Utilizadas
* **Python:** Linguagem de programação utilizada para desenvolver o sistema.
* **datetime:** Módulo Python para manipulação de datas e horas.
* **textwrap:** Módulo Python para formatação de texto.

### Gerenciador do Projeto
* **UV**

```markdown
## Funcionalidades

* **Cadastro de usuários:** Permite criar novos usuários com as seguintes informações:
    * Nome completo
    * CPF
    * Endereço completo
* **Gerenciamento de contas:** Permite realizar as seguintes operações:
    * Criar novas contas
    * Consultar saldo
    * Realizar depósitos
    * Realizar saques
    * Consultar extrato
=======
# Dbank2
>>>>>>> parent of 585c5be (Projeto)
