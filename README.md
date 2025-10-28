# 🏛️ SISTEMA BANCARIO

## Estrutura:
- classes.py
    - class Banco
    - class Cliente
    - class OperacoesFinanceiras (ABC)
    - class Conta (OperacoesFinanceiras)
    - class ContaCorrente(Conta)
    - class ContaPoupanca(Conta)
    
- funcoes.py
    - def gerente_cliente()
    - def gerente_senha()
    - def menu_gerente()
    - def gerenciar_clientes()
    - def gerenciar_contas()
    - def login_ou_cadastro_cliente()
    - def login_cliente()
    - def cadastro_cliente()
    - def menu_cliente()
    - def criar_conta()
    - def listar_clientes()
    - def listar_clientes_por()
    - def excluir_cliente()
    - def listar_contas()
    - def listar_contas_por_cliente()
    - def verificar_conta()
    - def deposito()
    - def saque()
    - def transferencia()
    - def consulta_saldo_extrato()
 
- app.py
  - gerente_cliente()

---
## Explicação classes
- **class Banco**
  A **classe Banco** foi criadapara gerenciar clientes e contas do sistema. Ela mantém listas de clientes e contas, permitindo cadastrar, localizar e controlar operações bancárias. Representa     uma agregação, pois os clientes podem existir fora do banco.

- **class Cliente**
  A **classe Cliente** foi criada para armazenar informações pessoais do cliente, como nome, CPF e contatos. Cada cliente pode possuir uma ou mais contas, estabelecendo uma associação com a       classe Conta. Facilita o gerenciamento das contas vinculadas ao cliente.

- **class OperacoesFinanceiras**
  A **classe OperacoesFinanceiras** foi criada como uma interface (ou contrato) para definir métodos obrigatórios relacionados a operações financeiras, como depositar(), sacar() e                 transferir().   Isso garante padronização entre diferentes tipos de conta.

- **class Conta**
  A **classe Conta** foi criada como classe base abstrata, representando o comportamento comum de todas as contas. Contém atributos como número da conta, saldo e cliente associado, além de        métodos genéricos como depósito, saque e transferência. Não pode ser instanciada diretamente, promovendo abstração e reutilização de código.

- **class ContaCorrente(Conta)**
  A **classe ContaCorrente** herda de Conta e representa contas correntes. Permite saques sem saldo mínimo, reimplementando o método sacar() da classe base. Demonstra o uso de herança e           polimorfismo, pois aproveita métodos comuns, mas ajusta comportamentos específicos.

- **class ContaPoupanca(Conta)**
  A **classe ContaPoupanca** herda de Conta e representa contas poupança. Possui regra de saldo mínimo (R$ 100,00) para saques, reimplementando o método sacar() com comportamento diferente da     conta corrente. Demonstra polimorfismo e garante maior controle financeiro.

---
## Explicação classes
- **def gerente_cliente()**  
  Exibe o menu inicial do sistema, permitindo escolher entre acesso de gerente ou cliente.

- **def gerente_senha()**  
  Solicita a senha do gerente e permite acesso ao menu do gerente caso a senha esteja correta.

- **def menu_gerente()**  
  Exibe as opções de gerenciamento do gerente: gerenciar clientes ou contas.

- **def gerenciar_clientes()**  
  Permite listar todos os clientes cadastrados ou excluir um cliente específico.

- **def gerenciar_contas()**  
  Permite listar todas as contas ou verificar detalhes de uma conta específica.

- **def login_ou_cadastro_cliente()**  
  Menu que permite ao usuário escolher entre fazer login ou se cadastrar como cliente.

- **def login_cliente()**  
  Realiza o login do cliente verificando nome e CPF, redirecionando para o menu do cliente em caso de sucesso.

- **def cadastro_cliente()**  
  Solicita dados do cliente, cria um objeto `Cliente`, cadastra-o no sistema e chama a função para criar a conta.

- **def menu_cliente()**  
  Exibe o menu do cliente, permitindo realizar depósito, saque, transferência, consultar extrato ou voltar ao menu principal.

- **def criar_conta()**  
  Cria uma conta (corrente ou poupança) para o cliente, vinculando-a ao mesmo e adicionando à lista de contas do banco.

- **def listar_clientes()**  
  Lista todos os clientes cadastrados, mostrando ID, nome, CPF e gênero.

- **def listar_clientes_por()**  
  Função complementar para listar clientes filtrando por algum critério (não implementada completamente no código fornecido).

- **def excluir_cliente()**  
  Remove um cliente da lista de clientes pelo nome, caso exista.

- **def listar_contas()**  
  Lista todas as contas cadastradas, mostrando ID, nome do cliente e saldo atual.

- **def listar_contas_por_cliente()**  
  Lista todas as contas de um cliente específico (não implementada completamente no código fornecido).

- **def verificar_conta()**  
  Exibe detalhes de uma conta específica, incluindo status de ativação e saldo.

- **def deposito()**  
  Realiza um depósito na conta vinculada ao cliente, atualizando o saldo.

- **def saque()**  
  Realiza um saque na conta do cliente, obedecendo às regras da conta (como saldo mínimo para poupança).

- **def transferencia()**  
  Realiza transferência entre contas de clientes diferentes, atualizando os saldos das duas contas envolvidas.

- **def consulta_saldo_extrato() / consulta_extrato()**  
  Exibe todas as operações registradas no extrato da conta e o saldo atual do cliente.

- **def getContaCliente()**  
  Função auxiliar que retorna a conta associada a um cliente, utilizada nas operações financeiras como depósito, saque e transferência.

---
## Explicação do código

### classes.py

```python
from abc import ABC, abstractmethod

class Banco: # criação da classe - Banco
    def __init__(self, nome: str, localizacao: str, cnpj: int): 
        self.__nome = nome 
        self.__localizacao = localizacao 
        self.__cnpj = cnpj 
        self.__clientes = []

    def getNome(self): 
        return self.__nome

    def getLocalizacao(self): 
        return self.__localizacao

    def getCnpj(self): 
        return self.__cnpj

    def getClientes(self): 
        return self.__clientes 
```

<p> - Primeiro, importamos o abstract method, após isso, criamos a classe Banco, com os atributos de nome (nome do banco), localização (localização do banco), cnpj (cnpj do banco)
 e uma lista com os clientes neste banco</p>
<p> - Posteriormente, criamos os get´s, (getNome(), getLocalizacao(), getCnpj() e getClientes()), metodos get´s que retornam o nome do banco, a sua localização, seu CNPJ e seus clientes</p>



```python
class Cliente:
    def __init__(self, id_: int, nome: str, idade: int, cpf: str, genero: str): 
        self.__id = id_ 
        self.__nome = nome 
        self.__idade = idade
        self.__cpf = cpf 
        self.__genero = genero 

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
```

<p> - Neste bloco criamos a classe Cliente, com os atributos como, id (ID do cliente), nome (nome do cliente), idade (idade do cliente), cpf (cpf do cliente) e genero (genero do cliente).</p>
<p> - Posteriormente, criamos os get´s, (getId(), getNome(), getIdade(), getCpf() e getGenero()), metodos get´s que retornam o ID do cliente, nome do cliente, a sua localização, seu CNPJ e seu gênero.</p>


```python
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
```

<p> - Criamos uma intarface OperacoesFinanceiras, pois todas as funções são '@abstractmethod'</p>
<p> - Agora, falando dos métodos, temos o 'sacar', que possui seu valor:float, 'depositar', um método que possui seu valor:float, 'transferir', que também possui seu valor:float. Todas essas funções não são utilizadas neste momente, por isso o 'pass', esses métodos serão utilizados em outros momentos.</p>



```python
class Conta(OperacoesFinanceiras):

    def __init__(self, id_: int, agencia: str, cliente: Cliente, saldo: float = 0, ativa: bool = True):
        self.__id = id_             
        self.__agencia = agencia    
        self.__cliente = cliente     
        self.__saldo = saldo        
        self.__ativa = ativa        
        self.__extrato = []

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


```

<p> - Primeira, criamos a classe Conta que herda de OperacoesFinanceiras, com seus atibutos, id (ID da conta), agencia (agência da conta), cliente (cliente que possui a conta), saldo (saldo da conta), ativa (ver se a conta esta ativa) e extrato (fatura da conta)</p>
<p> - Após isso criamos os get´s e suas funções (getId(), getAgencia(), getCliente(), getSaldo(), getAtiva(), getExtrato(), registrar_operacoes(), sacar(), depositar() e transferir()), os get´s returnam os valores denominados, as funções em partes, como registrar operação, registra as operaçõs, 'sacar' faz o saque, 'depositar' faz o deposito e 'tranferir faz a tranferencia'</p>



```python
class ContaCorrente(Conta):

    def __init__(self, id_, agencia, cliente, saldo: float = 0, ativa: bool = True):
        super().__init__(id_, agencia, cliente, saldo, ativa)
```

<p> - Criamos a classe ContaCorrente que herda de Conta, e utiliza o super(), e reutiliza seus atributos.</p>



```python
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
```

<p> - E pela ultima classe, temos ContaPoupanca que herda de Conta</p>
<p> - id da conta, agencia, conta do cliente, limite do saldo e se a conta está ativa</p>


---
## funcoes.py
```python
from classes import *  
from time import * 
import os 

clientes = [] 
contas = [] 


def gerente_cliente():
    while True:
        try:
            escolha = int(input("\n1 - GERENTE\n2 - CLIENTE\n0 - SAIR\n---> ")) 
            os.system("cls")
            match escolha:
                case 1: 
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
```

<p> - Para começo importamos as classes, importamos o time e sleep, para dar dalye entre o terminal e o import os, para fechar o terminal</p>
<p> - Agora, criamos as listas para guardas os clientes e contas</p>
<p> - Agora indo pelas funções, gerente_cliente() é um menu que escolhe ou ir para o cargo de gerente ou cliente, ou sair</p>



```python
def gerente_senha():
    os.system("cls")
    senha = "Gerente2025"
    entrada = input("Coloque a senha do gerente 0 para voltar\n---> ")
    if entrada == '0' or entrada == 0: 
        return gerente_cliente()
    
    elif entrada == senha:
        print("Entrando...") 
        os.system("pause")
        menu_gerente()

    else:
        print("Senha incorreta.")
        os.system("pause")
        gerente_senha()
```

<p> - Gerente_senha(), caso você escolha no menu o gerente, você possui uma senha 'Gerente2025', e então, você agora possui as permissões do gerente (caso acerte a senha).</p>


```python
def menu_gerente():
    os.system("cls")
    while True:
        print("=== MENU DO GERENTE ===\n")
        print("1 - Gerenciar clientes")
        print("2 - Gerenciar contas")
        print("0 - Voltar")
        escolha = input("---> ")
        match escolha:
            case "1":
                gerenciar_clientes()
            case "2":
                gerenciar_contas()
            case "0":
                return gerente_cliente()
            case _:
                print("Opção inválida.")
                os.system("pause")
```


<p> - Menu do gerente para ou escolher gerenciar os clientes ou gerenciar suas contas.</p>


```python
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
            case "2": 
                excluir_cliente()
            case "0":
                return menu_gerente()
            case _:
                print("Opção inválida.")
                os.system("pause")

```


<p> - Na função gerenciar_clientes, você está em um menu que pode listar ou excluir os clientes.</p>



```python
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
            case "2": 
                verificar_conta()
            case "0":
                return menu_gerente()
            case _:
                print("Opção inválida.")
                os.system("pause")
```


<p> - Em gerenciar_contas, o gerente pode listar as contas ou ver se elas estão ativas.</p>


```python
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
```


<p> - Em login_ou_cadastro_cliente, o usuário decide ou logar ou cadastrar.</p>



```python
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
    print("Cliente não encontrado.")
    os.system("pause")
    login_ou_cadastro_cliente()
```


<p> - Aqui no login, você coloca seu nome e cpf, e verificar se exsite essa conta ou não.</p>



```python
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

```


<p> - Em cadastrar, você coloca seu nome, cpf, idade e genero, e com verificações, então, caso o cpf possua um número diferente de 11 ele da erro.</p>



```python
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

```


<p - >Define se é conta corrente ou punpança</p>


```python
def listar_clientes():
    os.system("cls")
    if not clientes: # caso não houver nada em clientes
        print("Nenhum cliente cadastrado.")
        os.system("pause")
        return
    for c in clientes: # lista de clientes
        print(f"{c.getId()} - {c.getNome()} - {c.getCpf()} - {c.getGenero()}")
    os.system("pause")
```


<p> - Lista os clientes</p>



```python
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
```


<p> - Excluir clientes</p>



```python

def listar_contas():
    os.system("cls")
    if not contas: # lista de clientes
        print("Nenhuma conta cadastrada.")
        os.system("pause")
        return
    for c in contas: # lista de contas
        print(f"ID {c.getID()} - Cliente: {c.getCliente().getNome()} - Saldo: R${c.getSaldo():.2f}")
```


<p> - Listar as contas</p>


```python
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
```


<p> - Verifica se a conta esta ativa ou não.</p>


```python
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
```
<p> - Menu para o cliebte escolher se vai depositar, sacar dinheiro,  tranferir dinheiro ou ver seu extrato. </p>


```python
    def getContaCliente(cliente):
        os.system("cls")
        for c in contas:
            if c.getCliente() == cliente:
                return c 
        print("Nenhuma conta foi encontrada")
        return None
```

<p>Pesquisa os clientes que necessita</p>


```python
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
```
<p> - Primeiro esta função verifica se a conta esta ativa, caso estiver, o cliente deposita um valor.</p>


```python 
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
```
<p> - Primeiro esta função verifica se a conta esta ativa, caso estiver, o cliente vai escolher um valor para sacar.</p>


```python
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
```
<p> - Nesta função será feito uma transferência,  logo precisa de um conta origem e um destino, caso uma das contas nãoestiver ativa, haveráum erro, se não o usuário precisa digitar o cpf para que ache a conta destinada, para trasferir o valor</p>


```python 
def consulta_extrato(cliente):
    os.system("cls")
    conta = getContaCliente(cliente)
    if conta:
        print("\n--- EXTRATO ---")
        for extrato in conta.getExtrato():
            print(extrato)
        print(f"Saldo atual: R${conta.getSaldo():.2f}")
        os.system("pause")

```


<p> - Nesta ultima função, vemos o extrato, com o mesmo procedimento,  caso a conta estiver desativada, ira aparecer um erro, senão ira mostrar o extrato do cliente (caso houver).</p>



## app.py

```python
from funcoes import gerente_cliente

print("=== SEJA BEM-VINDO AO BANCO ===")
gerente_cliente()
```

<p>Inicialização do código, importando as funções</p>

---
# Diagrama de classes
<a href="https://miro.com/app/board/uXjVJ3dcNDI=/">Diagrama de classes</a>


