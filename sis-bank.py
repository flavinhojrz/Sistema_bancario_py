def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")
    return saldo

def sacar(saldo, valor):
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor de saque inválido!")
    return saldo

def exibir_extrato(saldo):
    print(f"Saldo atual: R${saldo:.2f}")

def menu():
    print("\n1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    return int(input("Escolha uma opção: "))

def main():
    saldo = 0
    while True:
        opcao = menu()
        if opcao == 1:
            valor = float(input("Informe o valor para depósito: "))
            saldo = depositar(saldo, valor)
        elif opcao == 2:
            valor = float(input("Informe o valor para saque: "))
            saldo = sacar(saldo, valor)
        elif opcao == 3:
            exibir_extrato(saldo)
        elif opcao == 4:
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
