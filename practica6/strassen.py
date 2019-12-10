import random
from random import randint
'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
ANALISIS DE ALGORITMOS
GRUPO: 3CV1
ALUMNOS:
Gutierrez Povedano Pablo
Reyes Valenzuela Alejandro
PROFESOR: BENJAMÍN LUNA BENOSO
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IMPLEMENTACIÓN DEL ALGORITMO DE STRASSEN
FECHA: 8/OCT/18
'''
k =0
l =0
#Llena matrices de manera aleatoria
def fillgrid(size):
	C = [[0 for j in range(0, size)] for i in range(0, size)]
	for i in range(0, size):
		for j in range(0, size):
			C[i][j] = randint(1,5)
	return C


def sumar(A,B):
	#Suma de matrices
	n = len(A)
	C = [[0 for j in range(0, n)] for i in range(0, n)]
	for i in range(0, n):
		for j in range(0, n):
			C[i][j] = A[i][j] + B[i][j]
	return C
	
def restar(A, B):
	#Resta de matrices
	n = len(A)
	C = [[0 for j in range(0, n)] for i in range(0, n)]
	for i in range(0, n):
		for j in range(0, n):
			C[i][j] = A[i][j] - B[i][j]
	return C

def producto(A, B):
	#Producto usual de matrices
	n = len(A)
	C = [[0 for i in range(n)] for j in range(n)]
	l+=1
	for i in range(n):
		for k in range(n):
			for j in range(n):
				C[i][j] += A[i][k] * B[k][j]
				l+=1
	return C

def Strassen(A,B):
	global k
	n = len(A)
	if n==2:
		k += 1
		return producto(A, B)
	else:
		#Obtenemos los nuevos tamaños de las matrices para reducir el trabajo
		tam = n//2
		a11 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		a12 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		a21 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		a22 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		b11 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		b12 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		b21 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		b22 = [[0 for j in range(0, tam)] for i in range(0, tam)]
		k += 1
		#Obtenemos los valores de A y de B para realizar las operaciones pertinentes
		for i in range(0, tam):
			for j in range(0, tam):
				a11[i][j] = A[i][j]          	#A11
				k += 1
				a12[i][j] = A[i][j + tam]    	#A12
				k += 1
				a21[i][j] = A[i + tam][j]    	#A21
				k += 1
				a22[i][j] = A[i + tam][j + tam] #A22
				k += 1

				b11[i][j] = B[i][j]           	#B11
				k += 1
				b12[i][j] = B[i][j + tam]    	#B12
				k += 1
				b21[i][j] = B[i + tam][j]    	#B21
				k += 1
				b22[i][j] = B[i + tam][j + tam] #B22
				k += 1

		auxA = sumar(a11, a22)
		k += 1
		auxB = sumar(b11, b22)
		k += 1
		p1 = Strassen(auxA, auxB) # p1 = (a11+a22) * (b11+b22)
		k += 1
		auxA = sumar(a21, a22) 
		k += 1     # a21 + a22
		p2 = Strassen(auxA, b11)  # p2 = (a21+a22) * (b11)
		k += 1
		auxB = restar(b12, b22) # b12 - b22
		k += 1
		p3 = Strassen(a11, auxB)  # p3 = (a11) * (b12 - b22)
		k += 1
		auxB = restar(b21, b11) # b21 - b11
		k += 1
		p4 = Strassen(a22, auxB)   # p4 = (a22) * (b21 - b11)
		k += 1
		auxA = sumar(a11, a12)      # a11 + a12
		k += 1
		p5 = Strassen(auxA, b22)  # p5 = (a11+a12) * (b22)
		k += 1
		auxA = restar(a21, a11) # a21 - a11
		k += 1
		auxB = sumar(b11, b12)      # b11 + b12
		k += 1
		p6 = Strassen(auxA, auxB) # p6 = (a21-a11) * (b11+b12)
		k += 1
		auxA = restar(a12, a22) # a12 - a22
		k += 1
		auxB = sumar(b21, b22)      # b21 + b22
		k += 1
		p7 = Strassen(auxA, auxB) # p7 = (a12-a22) * (b21+b22)
		k += 1
		# Obteniendo los valores de C11,C12,C21,C22
		c12 = sumar(p3, p5) # c12 = p3 + p5
		k += 1
		c21 = sumar(p2, p4)  # c21 = p2 + p4
		k += 1
		auxA = sumar(p1, p4) # p1 + p4
		k += 1
		auxB = sumar(auxA, p7) # p1 + p4 + p7
		k += 1
		c11 = restar(auxB, p5) # c11 = p1 + p4 - p5 + p7
		k += 1
		auxA = sumar(p1, p3) # p1 + p3
		k += 1
		auxB = sumar(auxA, p6) # p1 + p3 + p6
		k += 1
		c22 = restar(auxB, p2) # c22 = p1 + p3 - p2 + p6
		k += 1
		C = [[0 for j in range(0, n)] for i in range(0, n)]
		for i in range(0, tam):
			for j in range(0, tam):
				C[i][j] = c11[i][j]
				C[i][j + tam] = c12[i][j]
				C[i + tam][j] = c21[i][j]
				C[i + tam][j + tam] = c22[i][j]
		return C
def main():
	tam=8
	x=fillgrid(tam)
	y=fillgrid(tam)
	print("-----Matriz 1-----")
	for z in range(tam):
		print(x[z])
	print("-----Matriz 2-----")
	for z in range(tam):
		print(y[z])
	print("-----Producto-----")
	c=Strassen(x,y)
	for z in range(tam):
		print(c[z])
	print("-----DATOS ADICIONALES-----")
	print("Tamaño matriz:" +str(tam))
	print("Contador Strassen: "+str(k))


if __name__ == '__main__':
	main()
''' 
tamaños		k			l
2			1			15	
4			65			85
8			609			731			
16			4801		5021		
32			35681		39825				
64			257985		266305	
'''