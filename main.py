from datetime import datetime, timedelta
import textwrap

clientes = [
    {
        'cpf': '12345678900',
        'nome': 'João Silva',
        'endereco': {
            'logradouro': 'Rua das Flores',
            'numero': '123',
            'complemento': 'Apto 101',
            'bairro': 'Centro',
            'cidade': 'Contagem',
            'estado': 'MG'
        },
        'contas': [
            {
                'agencia': '0001',
                'numero': 1,
                'saldo': 1000.00,
                'extrato': [],
                'transacoes_diarias': 0,
                'saques_diarios': 0,
                'ultima_transacao': None
            }
        ]
    }
]

def limpar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    if not cpf.isdigit() or len(cpf) != 11:
        return None
    return cpf

def gerar_numero_conta():
    max_numero_conta = max((conta['numero'] for cliente in clientes for conta in cliente['contas']), default=0)
    return max_numero_conta + 1

def novo_usuario():
    cpf = input("Informe o CPF (somente números): ")
    cpf = limpar_cpf(cpf)
    if not cpf:
        print("\n@@@ Operação falhou! CPF inválido. @@@")
        return False
    if any(cliente['cpf'] == cpf for cliente in clientes):
        print("\n@@@ Operação falhou! CPF já cadastrado. @@@")
        return False
    nome = input("Informe o nome: ")
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    complemento = input("Informe o complemento: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado: ")
    numero_conta = gerar_numero_conta()
    cliente = {
        'cpf': cpf,
        'nome': nome,
        'endereco': {
            'logradouro': logradouro,
            'numero': numero,
            'complemento': complemento,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado
        },
        'contas': [
            {
                'agencia': '0001',
                'numero': numero_conta,
                'saldo': 0,
                'extrato': [],
                'transacoes_diarias': 0,
                'saques_diarios': 0,
                'ultima_transacao': None
            }
        ]
    }
    clientes.append(cliente)
    print(f"\n@@@ Usuário e conta {numero_conta} criados com sucesso. @@@")
    return True

def nova_conta():
    cpf = input("Informe o CPF do usuário: ")
    cpf = limpar_cpf(cpf)
    if not cpf:
        print("\n@@@ Operação falhou! CPF inválido. @@@")
        return False
    cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)
    if not cliente:
        print("\n@@@ Operação falhou! Usuário não encontrado. @@@")
        return False
    numero_conta = gerar_numero_conta()
    conta = {
        'agencia': '0001',
        'numero': numero_conta,
        'saldo': 0,
        'extrato': [],
        'transacoes_diarias': 0,
        'saques_diarios': 0,
        'ultima_transacao': None
    }
    cliente['contas'].append(conta)
    print(f"\n@@@ Conta {numero_conta} criada com sucesso. @@@")
    return True

def listar_contas(cliente):
    for conta in cliente['contas']:
        print(f"Conta: {conta['numero']}")

def selecionar_conta(cliente):
    if len(cliente['contas']) == 1:
        return cliente['contas'][0]
    listar_contas(cliente)
    numero_conta = int(input("Informe o número da conta: "))
    conta = next((conta for conta in cliente['contas'] if conta['numero'] == numero_conta), None)
    return conta

def verificar_transacoes_diarias(conta):
    if conta['ultima_transacao'] and conta['ultima_transacao'].date() != datetime.now().date():
        conta['transacoes_diarias'] = 0
        conta['saques_diarios'] = 0

def solicitar_valor(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor = valor.replace(',', '.')
            valor = float(valor)
            valor = abs(round(valor, 2))
            return valor
        except ValueError:
            print("Operação falhou! O valor informado é inválido. Tente novamente.")

def confirmar_operacao(mensagem):
    while True:
        confirmacao = input(mensagem).lower()
        if confirmacao in ['s', 'n']:
            return confirmacao
        print("Valor inválido! Insira 's' ou 'n'.")

def depositar(cpf, /):
    cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)
    if not cliente:
        print("\n@@@ Operação falhou! Usuário não encontrado. @@@")
        return
    conta = selecionar_conta(cliente)
    if not conta:
        print("\n@@@ Operação falhou! Conta não encontrada. @@@")
        return
    verificar_transacoes_diarias(conta)
    if conta['transacoes_diarias'] >= 10:
        print("\n@@@ Operação falhou! Limite diário de transações atingido. @@@")
        return
    valor = solicitar_valor("Informe o valor do depósito: ")
    confirmacao = confirmar_operacao(f"Você quer depositar R${valor:.2f}? (s/n): ")
    if confirmacao == 's':
        conta['saldo'] += valor
        conta['extrato'].append(f"Depósito: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        conta['transacoes_diarias'] += 1
        conta['ultima_transacao'] = datetime.now()
        print(f"\n@@@ Depósito de R$ {valor:.2f} realizado com sucesso. @@@")
    else:
        print("Depósito cancelado.")

def sacar(*, cpf):
    cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)
    if not cliente:
        print("\n@@@ Operação falhou! Usuário não encontrado. @@@")
        return
    conta = selecionar_conta(cliente)
    if not conta:
        print("\n@@@ Operação falhou! Conta não encontrada. @@@")
        return
    verificar_transacoes_diarias(conta)
    if conta['transacoes_diarias'] >= 10:
        print("\n@@@ Operação falhou! Limite diário de transações atingido. @@@")
        return
    if conta['saques_diarios'] >= 3:
        print("\n@@@ Operação falhou! Limite diário de saques atingido. @@@")
        return
    valor = solicitar_valor("Informe o valor do saque: ")
    if valor > conta['saldo']:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        return
    if valor > 500:
        print("\n@@@ Operação falhou! O valor do saque não pode exceder R$ 500,00. @@@")
        return
    confirmacao = confirmar_operacao(f"Você quer sacar R${valor:.2f}? (s/n): ")
    if confirmacao == 's':
        conta['saldo'] -= valor
        conta['extrato'].append(f"Saque: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        conta['transacoes_diarias'] += 1
        conta['saques_diarios'] += 1
        conta['ultima_transacao'] = datetime.now()
        print(f"\n@@@ Saque de R$ {valor:.2f} realizado com sucesso. @@@")
    else:
        print("Saque cancelado.")

def extrato(cpf, *, outro_argumento=None):
    cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)
    if not cliente:
        print("\n@@@ Operação falhou! Usuário não encontrado. @@@")
        return
    conta = selecionar_conta(cliente)
    if not conta:
        print("\n@@@ Operação falhou! Conta não encontrada. @@@")
        return
    print(f"\n================ EXTRATO - Conta {conta['numero']} ================")
    for transacao in conta['extrato']:
        print(textwrap.dedent(transacao))
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

def exibir_saldo(cpf):
    cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)
    if not cliente:
        print("\n@@@ Operação falhou! Usuário não encontrado. @@@")
        return
    conta = selecionar_conta(cliente)
    if not conta:
        print("\n@@@ Operação falhou! Conta não encontrada. @@@")
        return
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")

def menu():
    menu = f"""\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def iniciar_sistema():
    while True:
        opcao = menu()
        if opcao == 'nu':
            novo_usuario()
        elif opcao == 'nc':
            nova_conta()
        elif opcao in ['d', 's', 'e']:
            cpf = input("Informe o CPF: ")
            cpf = limpar_cpf(cpf)
            if not cpf:
                print("\n@@@ Operação falhou! CPF inválido. @@@")
                continue
            if opcao == 'd':
                depositar(cpf)
            elif opcao == 's':
                sacar(cpf=cpf)
            elif opcao == 'e':
                extrato(cpf, outro_argumento=None)
        elif opcao == 'lc':
            cpf = input("Informe o CPF: ")
            cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)
            if cliente:
                listar_contas(cliente)
            else:
                print("\n@@@ Operação falhou! Usuário não encontrado. @@@")
        elif opcao == 'q':
            print("\nAté logo!")
            break
        else:
            print("\n@@@ Operação inválida! Tente novamente. @@@")


iniciar_sistema()
