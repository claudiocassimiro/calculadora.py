num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
novo_valor = str(input("Deseja digitar outro valor? [S/N]: ").upper())
if novo_valor == "S":
	num3 = int(input("Digite outro valor: "))
	novo_valor2 = str(input("Deseja digitar outro valor? [S/N]: ").upper())
	if novo_valor2 == "S":
		num4 = int(input("Digite outro valor: "))
		print("Soma [1]")
		print("Subtração [2]")
		print("Divisão [3]")
		print("Multiplicação [4]")
		escolha = int(input("Digite o valor da operação desejada: "))
		if escolha == 1:
			print("A soma entre {} + {} + {} + {} = {}".	format(num1, num2, num3, num4, num1+num2+num3+num4))
		if escolha == 2:
			print("A subtração entre {} - {} - {} - {} = {}".format(num1, num2, num3, num4, num1-num2-num3-num4))
		if escolha == 3:
			print("A divisão entre {} / {} / {} / {} = {}".format(num1, num2, num3, num4, num1/num2/num3/num4))
		if escolha == 4:
			print("A multiplicação entre {} * {} * {} * {} = {}".format(num1, num2, num3, num4, num1*num2*num3*num4))
	else:
		print("Soma [1]")
		print("Subtração [2]")
		print("Divisão [3]")
		print("Multiplicação [4]")
		escolha = int(input("Digite o valor da operação desejada: "))
		if escolha == 1:
			print("A soma entre {} + {} + {} = {}".	format(num1, num2, num3, num1+num2+num3))
		if escolha == 2:
			print("A subtração entre {} - {} - {} = {}".format(num1, num2, num3, num1-num2-num3))
		if escolha == 3:
			print("A divisão entre {} / {} / {} = {}".format(num1, num2, num3, num1/num2/num3))
		if escolha == 4:
			print("A multiplicação entre {} * {} * {} = {}".format(num1, num2, num3, num1*num2*num3))
else:
	print("Soma [1]")
	print("Subtração [2]")
	print("Divisão [3]")
	print("Multiplicação [4]")
	escolha = int(input("Digite o valor da operação desejada: "))
	if escolha == 1:
		print("A soma entre {} + {} = {}".format(num1, num2, num1+num2))
	if escolha == 2:
		print("A subtração entre {} - {} = {}".format(num1, num2, num1-num2))
	if escolha == 3:
		print("A divisão entre {} / {} = {}".format(num1, num2, num1/num2))
	if escolha == 4:
		print("A multiplicação entre {} * {} = {}".format(num1, num2, num1*num2))