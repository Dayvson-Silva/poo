# Banco do Biu
print("==================== BEM-VINDO AO BANCO DO BIU ====================")
class Conta:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")


def criar_conta():
    numero_conta = int(input("Digite o número da conta: "))
    titular = input("Digite o nome do titular: ")
    saldo = float(input("Digite o saldo inicial (opcional): "))
    return Conta(numero_conta, titular, saldo)


def menu():
    print("\n--- Menu ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir saldo")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

if __name__ == "__main__":
    conta = Conta()

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == 3:
            conta.exibir_saldo()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")