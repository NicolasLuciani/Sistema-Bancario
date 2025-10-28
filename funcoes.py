from classes import *  # Importa todas as classes do arquivo classes.py
from time import * # Importa funções de tempo, se necessário
import os # Importa funções do sistema operacional (limpar tela, pausar, etc.)

clientes = [] # lista de clientes
contas = [] # lista de contas

# -------------------------------------------------------------------
def gerente_cliente():
    while True:
        try:
            escolha = int(input("\n1 - GERENTE\n2 - CLIENTE\n0 - SAIR\n---> ")) 
            os.system("cls")
            match escolha:
                case 1: # função de menu entre o gerente e o cliente
                    gerente_senha()
                case 2:
                    login_ou_cadastro_cliente()
                case 0:
                    break
                case _:
                    print("Escolha inválida")
                    os.system("pause")

        except ValueError:
            print("Digite apenas numeros.")
            os.system("pause")


# ---------------- GERENTE ----------------
def gerente_senha():
    os.system("cls")
    senha = "Gerente2025" # senha do gerente
    entrada = input("Coloque a senha do gerente 0 para voltar\n---> ")
    if entrada == '0' or entrada == 0: # se gerente for igual a 0 ele volta
        return gerente_cliente()
    
    elif entrada == senha:
        print("Entrando...") # caso acerte a senha, ele entra
        os.system("pause")
        menu_gerente()

    else:
        print("Senha incorreta.")
        os.system("pause") # caso erre a senha, ele falha
        gerente_senha()


def menu_gerente():
    os.system("cls")
    while True:
        print("=== MENU DO GERENTE ===\n")
        print("1 - Gerenciar clientes")
        print("2 - Gerenciar contas")
        print("0 - Voltar")
        escolha = input("---> ")
        match escolha:
            case "1": # menu para o gerente gereciar os clientes e suas contas
                gerenciar_clientes()
            case "2":
                gerenciar_contas()
            case "0":
                return gerente_cliente()
            case _:
                print("Opção inválida.")
                os.system("pause")


def gerenciar_clientes():
    os.system("cls")
    while True:
        print("\n--- GERENCIAR CLIENTES ---")
        print("1 - Listar clientes")
        print("2 - Excluir cliente")
        print("0 - Voltar")
        escolha = input("--> ")
        match escolha:
            case "1":
                listar_clientes()
            case "2": # menu para listar ou excluir os clientes
                excluir_cliente()
            case "0":
                return menu_gerente()
            case _:
                print("Opção inválida.")
                os.system("pause")


def gerenciar_contas():
    os.system("cls")
    while True:
        print("\n--- GERENCIAR CONTAS ---")
        print("1 - Listar contas")
        print("2 - Verificar conta")
        print("0 - Voltar")
        escolha = input("--> ")
        match escolha:
            case "1":
                listar_contas()
            case "2": # menu para listar as contas, ou verifca-las
                verificar_conta()
            case "0":
                return menu_gerente()
            case _:
                print("Opção inválida.")
                os.system("pause")


# ---------------- CLIENTE ----------------
def login_ou_cadastro_cliente():
    os.system("cls")
    while True:
        print("=-=-=-= TELA DE LOGIN OU CADASTRO =-=-=-=")
        print("Escolha")
        try:
            escolha = int(input("\n1 - Login\n2 - Cadastro\n--> "))
            match escolha:
                case 1:
                    login_cliente()
                    break
                case 2: # menu para o cliente logar ou cadastrar
                    cadastro_cliente()
                    break
                case _:
                    print("Opção inválida.")
                    os.system("pause") # opção não existe
        except Exception as e:
            print(f"Houve um erro {e}")
            os.system("pause")


def login_cliente():
    os.system("cls")
    usuario = input("Nome: ")
    cpf = input("CPF: ")
    for c in clientes:
        if c.getNome() == usuario and c.getCpf() == cpf:
            print(f"Bem-vindo, {usuario}!")
            os.system("pause")
            menu_cliente(c)
            return
    print("Cliente não encontrado.") # caso logar e não houver o cadastro, falhara
    os.system("pause")
    login_ou_cadastro_cliente()


def cadastro_cliente():
    os.system("cls")
    while True:
        try:
            nome = input("Nome: ") # nome
            idade = int(input("Idade: ")) # idade
            cpf = input("CPF(somente numeros): ") # cpf
            genero = input("Gênero: ") # genero
            
            if nome == "": # caso não houver nada no nome, erro
                print("Digite um genero para validar!")
                os.system("pause")
                continue

            elif idade <= 0: # caso idade menor ou igual a 0, erro
                print("Idade inválida.")
                os.system("pause")
                continue

            elif len(cpf) != 11: # caso o cpf não houver 11 digitos, erro
                print("O CPF deve conter 11 dígitos.")
                os.system("pause")
                continue

            elif genero == "": # caso não houver nada no genero, erro
                print("Digite um genero para validar!")
                os.system("pause")
                continue

            id_cliente = len(clientes) + 1
            cliente = Cliente(id_cliente, nome, idade, cpf, genero)
            clientes.append(cliente)

            print("Cliente cadastrado com sucesso")
            os.system("pause")
            criar_conta(cliente)
            menu_cliente(cliente)
            

        except Exception as e:
            print(f"Houve um erro {e}")
            os.system("pause")
            cadastro_cliente()


# ---------------- CONTA ----------------
def criar_conta(cliente):
    os.system("cls")
    while True:
        tipo = input("1 - Conta Corrente\n2 - Conta Poupança\n--> ")

        id_conta = len(contas) + 1

        match tipo:
            case "1":
                conta = ContaCorrente(id_conta, cliente)
                print("Agência atribuída automaticamente: 0001")
            case "2":
                conta = ContaPoupanca(id_conta, cliente)
                print("Agência atribuída automaticamente: 0002")
            case _:
                print("Opção inválida. Digite 1 ou 2.")
                os.system("pause")
                os.system("cls")
                continue

        contas.append(conta)
        print(f"Conta {id_conta} criada para {cliente.getNome()}.")
        os.system("pause")
        break


# ---------------- OPERAÇÕES ----------------
def listar_clientes():
    os.system("cls")
    if not clientes: # caso não houver nada em clientes
        print("Nenhum cliente cadastrado.")
        os.system("pause")
        return
    for c in clientes: # lista de clientes
        print(f"{c.getId()} - {c.getNome()} - {c.getCpf()} - {c.getGenero()}")
    os.system("pause")



def excluir_cliente():
    os.system("cls")
    nome = input("Nome do cliente a excluir: ")
    for c in clientes: # exclusão de clientes
        if c.getNome() == nome:
            clientes.remove(c)
            print("Cliente removido.") # cliente removido
            os.system("pause")
            return
    print("Cliente não encontrado.")
    os.system("pause")


def listar_contas():
    os.system("cls")
    if not contas: # lista de clientes
        print("Nenhuma conta cadastrada.")
        os.system("pause")
        return
    for c in contas: # lista de contas
        print(f"ID {c.getID()} - Cliente: {c.getCliente().getNome()} - Saldo: R${c.getSaldo():.2f}")


def verificar_conta():
    os.system("cls")
    try:
        num = int(input("ID da conta: "))
        for c in contas:
            if c.getID() == num: # verifica se a conta esta  ativa
                print(f"Conta ativa: {c.getAtiva()} - Saldo: R${c.getSaldo():.2f}")
                return # caso esteja ativa, lista das contas com |ativa e saldo|
        print("Conta não encontrada.")
        os.system("pause")
        
    except Exception as e:
        print(f"Houve um erro {e}")
        os.system("pause")


# ---------------- OPERAÇÕES CLIENTE ----------------
def menu_cliente(cliente):
    os.system("cls")
    while True:
        try:
            print(f"\n=== MENU CLIENTE ({cliente.getNome()}) ===")
            print("1 - Depósito") # deposito
            print("2 - Saque") # saque
            print("3 - Transferência") # transferencia
            print("4 - Extrato") # extrato
            print("5 - Voltar") # volta ao anterior
            escolha = input("--> ")
            match escolha:
                case "1":
                    deposito(cliente)
                case "2":
                    saque(cliente)
                case "3": # menu para trasferencias bancarias
                    transferencia(cliente)
                case "4":
                    consulta_extrato(cliente)
                case "5":
                    return gerente_cliente()
                case _:
                    print("Opção inválida.")
                    os.system("pause")
        
        except Exception as e:
            print(f"Houve um erro {e}")
            os.system("pause")


def getContaCliente(cliente):
    os.system("cls")
    for c in contas:
        if c.getCliente() == cliente:
            return c # procura de clientes
    print("Nenhuma conta foi encontrada")
    return None


def deposito(cliente):
    os.system("cls")
    conta = getContaCliente(cliente)
    if conta:
        try:
            valor = float(input("Digite o valor\n--->"))
            conta.depositar(valor) # depos
            print(f"Depósito realizado com sucesso!\nSaldo: R${conta.getSaldo():.2f}")
            os.system("pause")

        except ValueError:
            print("Valor inválido.")
            os.system("pause")
    else:
        print("Essa conta não está ativa!")
        os.system("pause")


def saque(cliente):
    os.system("cls")
    conta = getContaCliente(cliente)
    if conta:        
        try: 
            valor = float(input("Digite o valor\n--->"))
            conta.sacar(valor)
            print(f"Saldo atual: R${conta.getSaldo():.2f}")
            os.system("pause")
            
        except ValueError:
            print("Valor inválido.")
            os.system("pause")

    else:
        print("Essa conta não está ativa!")
        os.system("pause")


def transferencia(cliente):
    os.system("cls")
    conta_origem = getContaCliente(cliente)
    if not conta_origem:
        print("Não há nenhuma conta ativa!")
        os.system("pause")
        return

    cpf_destino = input("Digite o CPF do destinatário (somente números): ")
    if not cpf_destino.isdigit():
        print("CPF inválido! Digite apenas números.")
        os.system("pause")
        return

    conta_destino = None
    for c_d in contas:
        if c_d.getCliente().getCpf() == cpf_destino:
            conta_destino = c_d
            break

    if not conta_destino:
        print("Destino não encontrado.")
        os.system("pause")
        return

    try:
        valor = float(input("Digite o valor da transferência:\n---> "))
        if valor <= 0:
            print("Valor inválido. Deve ser maior que zero.")
            os.system("pause")
            return

        conta_origem.transferir(valor, conta_destino)
        print("Transferência realizada com sucesso!")
        os.system("pause")

    except ValueError:
        print("Valor inválido.")
        os.system("pause")


def consulta_extrato(cliente):
    os.system("cls")
    conta = getContaCliente(cliente)
    if conta:
        print("\n--- EXTRATO ---")
        for extrato in conta.getExtrato():
            print(extrato)
        print(f"Saldo atual: R${conta.getSaldo():.2f}")
        os.system("pause")
