import textwrap

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.limite = 500
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor, limite_saques):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self, agencia):
        self.agencia = agencia
        self.contas = []
        self.usuarios = []

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print("=== Usuário criado com sucesso! ===")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta(self, cpf):
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            numero_conta = len(self.contas) + 1
            conta = Conta(self.agencia, numero_conta, usuario)
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
            return conta
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(f"Agência:\t{conta.agencia}")
            print(f"C/C:\t\t{conta.numero_conta}")
            print(f"Titular:\t{conta.usuario.nome}")
            print("=" * 100)

def menu():
    menu = """\n
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

def main():
    banco = Banco(agencia="0001")
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do depósito: "))
            conta = banco.contas[numero_conta - 1]  # A indexação começa em 0
            conta.depositar(valor)

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do saque: "))
            conta = banco.contas[numero_conta - 1]  # A indexação começa em 0
            conta.sacar(valor, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = banco.contas[numero_conta - 1]  # A indexação começa em 0
            conta.exibir_extrato()

        elif opcao == "nu":
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            cpf = input("Informe o CPF (somente número): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            banco.criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário para criar a conta: ")
            banco.criar_conta(cpf)

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
