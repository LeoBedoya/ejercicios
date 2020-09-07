def mostrarlista(l1):#Recorre la lista  y la muestra
	for nfilas in l1:
		print(nfilas)

def sumdiagonales(l1):
	n=len(l1)
	diag=[]
	global suma_diag_dere 
	suma_diag_dere=0
	global suma_diag_izq
	suma_diag_izq=0
	for ind1 in range(nfilas):
		suma_diag_dere=suma_diag_dere+l1[ind1][ind1]				
		for ind2 in range(ncolumnas):
			if (ind1+ind2==n-1):
				suma_diag_izq=suma_diag_izq+l1[ind1][ind2]				
	print("La diagonal derecha:",suma_diag_dere)
	print("La diagonal izquierda:",suma_diag_izq,)
	if suma_diag_dere == suma_diag_izq:
		print("Las diagonales son numeros iguales\n")		
	else:
		print("Las diagonales no son iguales\n")

def sumnuevafila(nuevafila):#Verifica y si los numeros de la fila de abajo son iguales
	suma3=0
	global di
	co=len(nuevafila)
	for i in nuevafila:
		suma3= suma3 + i
		di=suma3//co
	if i == di:
		print("** los numeros de la fila de abajo son iguales **")
	elif i != di:
		print("Los numeros de la fila abajo no son iguales")
	return di

l1=[]#lista principal
cont=0
puntos=0
sumaultimacol=0	
nfilas= len(l1) #no cambiara de tamaño
ncolumnas= len(l1) #no cambiara de tamaño
nfilas= int(input("Digite numero de filas: "))
ncolumnas = int(input("Digite numero de columnas: "))

for ind1 in range(nfilas): #numero de filas  [[1,2][1,2]] matriz 2x2
	l1.append([])
	nuevafila=[]	
	for ind2 in range(ncolumnas):
		num=int(input("Digite numeros para llenar la matriz: "))
		l1[ind1].append(num)#Agrega los  numeros a la lista
		suma2=sum(nfilas[ind2] for nfilas in l1)#suma las columnas
		global contador1
		contador1 = 0 + suma2 #Valor a ingresar en la columna nueva
		nuevafila.append(contador1)
	if ind1 == ind1: #suma la primera fila y la almacena y asi sucesivamente
		suma=sum(l1[ind1])
		contador = 0 +suma
		l1[ind1].append(contador)
	
sumaultimacol=((sum(nuevafila)))			
mostrarlista(l1)
print(nuevafila,sumaultimacol)
sumdiagonales(l1)

if nfilas == ncolumnas:
	print("!* Es cuadratica *!\n")
else:
	print("No es cuadratica\n")

print(sumnuevafila(nuevafila))

if suma_diag_dere & suma_diag_izq == contador1 & di : #Condiciones para que sea un cuadro magico
	print("!! Es un Cuadro Magico !!")
else:
	print("No es un cuadro magico")