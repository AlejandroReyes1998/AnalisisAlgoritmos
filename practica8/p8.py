# -*- coding: utf-8 -*-
'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
ANALISIS DE ALGORITMOS
GRUPO: 3CV1
ALUMNOS:
Reyes Valenzuela Alejandro
PROFESOR: BENJAMÍN LUNA BENOSO
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Imprelemntación de los algoritmos de la búsqueda del producto óptimo de matrices e
impresión de producto de matrices 
FECHA: 8/NOV/18
'''
def MatrixSec(A):
	#Función que realiza el producto de manera óptima mediante los tamaños asignados previamente
	n= len(A)
	m = [[0 for x in range(n)] for x in range(n)]
	s = [[0 for x in range(n)] for x in range(n)]
	for i in range(1,n):
		m[i][i] = 0
	for L in range(2,n):
		for i in range(1,n-L+1):
			j = i+L-1
			m[i][j]=10000000
			for k in range(i,j):
				q=m[i][k]+m[k+1][j]+A[i-1]*A[k]*A[j]
				if q<m[i][j]:
					m[i][j]=q
					s[i][j]=k
	print("Configuración óptima de producto de matrices: ")
	IPO(1,n-1,n,s)
	print("")
	print("Minimo numero de multiplicaciones: %d" % m[1][n-1])

def IPO(i,j,n,s):
	"""Función que imprime el orden correcto de parentesis en la multiplicacion."""
	if i == j:
		print("A"+str(i)),
		return
	print("("),
	IPO(i,s[i][j],n,s)
	IPO(s[i][j]+1,j,n,s)
	print(")"),

def main():
	A = [3,6,8,2,4]
	print("Tamaños Matrices")
	print(A)
	MatrixSec(A)

if __name__ == '__main__':
	main()