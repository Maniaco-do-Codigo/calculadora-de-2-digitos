num1 = float(input("escolha um numero: "))
sinal = input("escolha a operação [+ - / *]: ")
num2 = float(input("escolha outro numero: "))


soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

if (sinal == "+"):
	print(num1, "+", num2, "=", soma)

elif (sinal == "-"):
	print(num1, "-", num2, "=", subtracao)

elif (sinal == "/"):
	print(num1, "/", num2, "=", divisao)

elif (sinal == "*"):
	print(num1, "*", num2, "=", multiplicacao)

else:
	print("ocorreu algum erro, tente novamente")