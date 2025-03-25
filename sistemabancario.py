# Função para validar se o valor é numérico e maior que 0
def obter_valor():
    while True:
        try:
            valor = float(input("Informe o valor: "))
            if valor > 0:
                return valor
            else:
                print("Operação falhou! O valor deve ser maior que zero.")
        except ValueError:
            print("Operação falhou! O valor informado não é válido.")

# Função para realizar o depósito
def depositar(saldo, extrato):
    valor = obter_valor()
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

# Função para realizar o saque
def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = obter_valor()

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função do menu do sistema
def menu():
    return input("""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo... Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
