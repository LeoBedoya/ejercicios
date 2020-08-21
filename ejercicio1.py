contador = 0
nuevo_rango = range(0,101)
for num in nuevo_rango:
	if num % 2!=0:
		print(num)
		contador += 1
print("la cantidad de numeros son: ",contador)
	