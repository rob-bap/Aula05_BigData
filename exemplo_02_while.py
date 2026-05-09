contador = 0
while contador < 5: 
    print(f"\nOperação {contador + 1}")
    numero = float(input("Digite um número: "))
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2
    print(f"\nO dobro de {numero} é {dobro:.2f}")
    print(f"O triplo de {numero} é {triplo:.2f}")
    print(f"O quadrado de {numero} é {quadrado:.2f}")
    contador += 1
print("\nOperação Concluída")