print("{} calculadora_soma.py {}".format("="*12, "="*12))
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
outro_valor = str(input("Deseja digitar mais um valor? [S/N]: " ).upper())
if outro_valor == "S":
    num3 = int(input("Digite outro valor: "))
    outro_valor2 = str(input("Deseja digitar mais um valor? [S/N]: " ).upper())
    if outro_valor2 == "S":
        num4 = int(input("Digite outro valor: "))
        print("O resultado da soma entre os quatros valores é igual a {}.".format(num1 + num2 + num3 + num4))
    else:
        print("O resultado da soma entre os três valores é igual a {}.".format(num1 + num2 + num3))
if outro_valor != "S":
    print("O resultado da soma entre os dois valores é igual a {}.".format(num1 + num2))
print("{} calculadora_soma.py {}".format("="*12, "="*12))