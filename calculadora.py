def suma(num1,num2):
		return num1 + num2
def resta(num1,num2):
	return num1 - num2
def multi(num1,num2):
	return num1 * num2
def divi(num1,num2):
	if num2 == 0:
		print("No se puede dividir entre 0")
	else:
		return num1 / num2
num1 = int(input("Digite numero 1 \n"))#solo numero
num2 = int(input("Digite numero 2\n")) #solo numero
op   = int(input("Digite operacion a realizar\n 1-sumar\n 2-restar \n 3-multiplicar \n 4-dividir\n")) #solo numero
if op == 1: 
	resul=suma(num1,num2)
	print("la suma es:",resul)
elif op == 2:
	resul=resta(num1,num2)
	print("La resta es:",resul)
elif op == 3:
	resul=multi(num1,num2)
	print("La Multiplicacion es:",resul)
elif op == 4:
	resul=divi(num1,num2)
	print("La division es:",resul)