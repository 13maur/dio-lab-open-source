def exibir_menu():
    """Função para exibir o menu de opções."""
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

def obter_entrada(simulacao=None):
    """Função para obter a entrada do usuário de maneira segura, suportando simulação."""
    opcoes_validas = {"d", "s", "e", "q"}
    if simulacao:
        return simulacao.pop(0)
    return "q"

def realizar_deposito(saldo, extrato, valor):
    """Função para realizar o depósito e atualizar o saldo e extrato."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def realizar_saque(saldo, limite, extrato, numero_saques, LIMITE_SAQUES, valor):
    """Função para realizar o saque e atualizar saldo, extrato e o número de saques."""
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(extrato, saldo):
    """Função para exibir o extrato e o saldo."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main(simulacao=None):
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print(exibir_menu())
        opcao = obter_entrada(simulacao)
        
        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato, 100)  # Simulando depósito de 100
        elif opcao == "s":
            saldo, extrato, numero_saques = realizar_saque(saldo, limite, extrato, numero_saques, LIMITE_SAQUES, 50)  # Simulando saque de 50
        elif opcao == "e":
            exibir_extrato(extrato, saldo)
        elif opcao == "q":
            print("Saindo... Até logo!")
            break

if __name__ == "__main__":
