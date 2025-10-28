from abc import ABC, abstractmethod  # Importa suporte para classes abstratas


class Banco:

    def __init__(self, nome: str, localizacao: str, cnpj: int):
        # Atributos do banco
        self.__nome = nome # Nome do banco
        self.__localizacao = localizacao # Localização ou cidade
        self.__cnpj = cnpj # CNPJ do banco
        self.__clientes = [] # Lista de clientes cadastrados

    # ------------------------ Métodos Get ------------------------
    def getNome(self): # Retorna o nome do banco
        return self.__nome

    def getLocalizacao(self): # Retorna a localização do banco
        return self.__localizacao

    def getCnpj(self): # Retorna o CNPJ do banco
        return self.__cnpj

    def getClientes(self):
        return self.__clientes


class Cliente:

    def __init__(self, id_: int, nome: str, idade: int, cpf: str, genero: str):
        # Atributos privados do cliente
        self.__id = id_            # ID único do cliente
        self.__nome = nome         # Nome completo
        self.__idade = idade       # Idade do cliente
        self.__cpf = cpf           # CPF
        self.__genero = genero     # Gênero (M/F/Outro)

    # ------------------------ Métodos Get ------------------------
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getCpf(self):
        return self.__cpf

    def getGenero(self):
        return self.__genero


class OperacoesFinanceiras(ABC):

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod
    def transferir(self, valor: float, destino):
        pass


class Conta(OperacoesFinanceiras):

    def __init__(self, id_: int, agencia: str, cliente: Cliente, saldo: float = 0, ativa: bool = True):
        # Atributos privados da conta
        self.__id = id_              # ID da conta
        self.__agencia = agencia     # Número da agência
        self.__cliente = cliente     # Objeto do tipo Cliente
        self.__saldo = saldo         # Saldo atual
        self.__ativa = ativa         # Status da conta
        self.__extrato = []          # Lista de operações (histórico)

    # ------------------------ Métodos Get ------------------------
    def getID(self):
        return self.__id

    def getAgencia(self):
        return self.__agencia

    def getCliente(self):
        return self.__cliente

    def getSaldo(self):
        return self.__saldo

    def getAtiva(self):
        return self.__ativa

    def getExtrato(self):
        return self.__extrato

    # ------------------------ Métodos de Operações ------------------------
    def registrar_operacao(self, descricao: str, valor: float):
        self.__extrato.append(f"{descricao}: R${valor:.2f}")

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor inválido. O saque deve ser maior que zero.")
            return

        if valor <= self.__saldo:
            self.__saldo -= valor
            self.registrar_operacao("Saque", -valor)
        else:
            print("Saldo insuficiente para o saque.")

    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor inválido. O depósito deve ser maior que zero.")
            return

        self.__saldo += valor
        self.registrar_operacao("Depósito", valor)

    def transferir(self, valor: float, destino):
        if valor <= 0:
            print("Valor inválido. A transferência deve ser maior que zero.")
            return

        if valor <= self.__saldo:
            self.__saldo -= valor
            self.registrar_operacao(f"Transferência para {destino.getCliente().getNome()}", -valor)
            destino.depositar(valor)
        else:
            print("Saldo insuficiente para transferência.")


class ContaCorrente(Conta):

    def __init__(self, id_, agencia, cliente, saldo: float = 0, ativa: bool = True):
        super().__init__(id_, agencia, cliente, saldo, ativa)
        # Nenhum atributo adicional é necessário, herda tudo de Conta.


class ContaPoupanca(Conta):

    def __init__(self, id_, agencia, cliente, limite: float = 100.0, saldo: float = 0, ativa: bool = True):
        super().__init__(id_, agencia, cliente, saldo, ativa)
        self.__limite = limite  # Valor mínimo que deve permanecer na conta

    def getLimite(self):
        return self.__limite

    def sacar(self, valor: float):
        if self.getSaldo() - valor >= self.__limite:
            super().sacar(valor)
        else:
            print(f"É necessário manter pelo menos R${self.__limite:.2f} na conta para sacar.")
