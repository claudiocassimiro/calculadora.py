print("{}Calculadora.py{}".format("=" * 6, "=" * 6))

num1 = float(input("Digite um valor: "))

num2 = float(input("Digite outro valor: "))

outro_valor = str(input("Deseja digitar outro valor? [S/N]: ").upper())

if outro_valor == "S":
    num3 = float(input("Digite o terceiro valor: "))

else:
    print("Digite [1] para Soma")
    print("Digite [2] Subtração")
    print("Digite [3] Divisão")
    print("Digite [4] Multiplicação")
    operacao = int(input("Qual a operação desejada?: "))

    if operacao == 1:
        print(num1 + num2)
        

    if operacao == 2:
        print(num1 - num2) 

    if operacao == 3:
        print(num1 / num2) 

    if operacao == 4:
        print(num1 * num2)

outro_valor2 = str(input("Deseja digitar outro valor? [S/N]: ").upper())

if outro_valor2 == "S":
    num4 = float(input("Digite o quarto valor: "))

    print("Digite [1] para Soma")
    print("Digite [2] Subtração")
    print("Digite [3] Divisão")
    print("Digite [4] Multiplicação")
    operacao = int(input("Qual a operação desejada?: "))

    if operacao == 1:
        print(num1 + num2 + num3 + num4)

    if operacao == 2:
        print(num1 - num2 - num3 - num4)

    if operacao == 3:
        print(num1 / num2 / num3 / num4)

    if operacao == 4:
        print(num1 * num2 * num3 * num4)

else:
    print("Digite [1] para Soma")
    print("Digite [2] Subtração")
    print("Digite [3] Divisão")
    print("Digite [4] Multiplicação")
    operacao = int(input("Qual a operação desejada?: "))

        if operacao == 1:
            print(num1 + num2 + num3)

        if operacao == 2:
            print(num1 - num2 - num3)

        if operacao == 3:
            print(num1 / num2 / num3)

        if operacao == 4:
            print(num1 * num2 * num3)

print("{}Calculadora.py{}".format("=" * 6, "=" * 6))