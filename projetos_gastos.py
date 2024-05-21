print("*****************CALCLADORA DE GASTOS MENSAIS********************")

def calcular_gastos_mensais():
    # Solicita ao usuário que insira os gastos mensais
    conta_agua = float(input("Digite o valor da conta de água: "))
    conta_luz = float(input("Digite o valor da conta de luz: "))
    conta_internet = float(input("Digite o valor da conta de internet: "))
    compras_mes = float(input("Digite o valor das compras do mês: "))

    # Calcula o total dos gastos mensais
    total_gastos = conta_agua + conta_luz + conta_internet + compras_mes


    # Imprime os resultados na tela
    print("\nResumo dos Gastos Mensais:")
    print(f"Conta de Água: R$ {conta_agua:.2f}")
    print(f"Conta de Luz: R$ {conta_luz:.2f}")
    print(f"Conta de Internet: R$ {conta_internet:.2f}")
    print(f"Compras do Mês: R$ {compras_mes:.2f}")
    print("-" * 20)
    print(f"Total dos Gastos: R$ {total_gastos:.2f}")

def main():
    print("Bem-vindo ao Programa de Cálculo de Gastos Mensais!\n")
    calcular_gastos_mensais()

if __name__ == "__main__":
    main() 