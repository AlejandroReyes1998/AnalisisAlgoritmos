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
IMPLEMENTACIÓN DEL ALGORITMO DE BUCKET SORT
FECHA: 15/OCT/18
'''
k=0
def bucket_sort(A):
	global k
	maximo = max(A)
	k=k+1
	tamarray = len(A)
	k=k+1
	TAM = maximo/tamarray
	k=k+1
	buckets = [[] for _ in range(tamarray)]
	for i in range(tamarray):
		j = int(A[i]/TAM)
		k=k+1
		if j != tamarray:
			buckets[j].append(A[i])
			k=k+1
		else:
			buckets[tamarray - 1].append(A[i])
			k=k+1
 
	for i in range(tamarray):
		insertion_sort(buckets[i])
		k=k+1
 
	ordenado = []
	for i in range(tamarray):
		ordenado = ordenado + buckets[i]
		k=k+1
 
	return ordenado
#Nos auxiliamos de insertion sort para ordenar los casilleros
def insertion_sort(A):
	for i in range(1, len(A)):
		aux = A[i]
		j = i - 1
		while (j >= 0 and aux < A[j]):
			A[j + 1] = A[j]
			j = j - 1
		A[j + 1] = aux

def main():
	global k
	tam=16
	print("Tamaño Arreglo: "+str(tam))
	A = [1000000,1000]
	print("Arreglo Original")
	print(A)
	sorted_list = bucket_sort(A)
	print('Arreglo Ordenado')
	print(sorted_list)
	print("")
	print("Pasos: "+str(k))

if __name__ == '__main__':
	main()
"""
Mejor caso
n-k
1-7
2-11
3-15
4-19
5-23
6-27
7-31
8-35
9-39
10-43
"""