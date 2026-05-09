for contador in range(3):
    print(f"\nCliente número {contador + 1}")
    compra1 = float(input("Digite o valor da sua primeira compra: R$"))
    compra2 = float(input("Digite o valor da sua primeira compra: R$"))
    valor_total = compra1 + compra2
    print(f"O valor total da sua compra foi de R${valor_total}")