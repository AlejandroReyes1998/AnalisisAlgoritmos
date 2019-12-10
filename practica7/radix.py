# -*- coding: utf-8 -*-
k =0
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
IMPLEMENTACIÓN DEL ALGORITMO DE RADIX SORT
FECHA: 15/OCT/18
'''
#Función que realiza el ordenamiento basándose en el número máximo de dígitos que contenga el arreglo
#Este algoritmo tiene complejidad O(n)
def countingSort(arr, exp1): 
 	#Obtenemos el tamaño del arreglo 
	n = len(arr) 
	#Generemos el arreglo de salida 
	output = [0] * (n) 
	#Generamos arreglo que se encargará de contar los dígitos de cualquier elemento
	count = [0] * (10)  
	#Guardamos los tamaños de los elementos
	for i in range(0, n): 
		index = (arr[i]/exp1) 
		count[ (index)%10 ] += 1
	#Actualizamos el arreglo con el tamaño del elemento actual
	for i in range(1,10): 
		count[i] += count[i-1] 
	#Llenamos el arreglo de salida
	i = n-1
	while i>=0: 
		index = (arr[i]/exp1) 
		output[ count[ (index)%10 ] - 1] = arr[i] 
		count[ (index)%10 ] -= 1
		i -= 1 
	#
	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 
  
#Algoritmo radixsort
def radixSort(arr):
	global k
	#Encuentra el máximo elemento de un arreglo
	max1 = max(arr)
	k += 1
	#Realizamos el ordenamiento para todos los elementos, y calculamos el tamaño en potencias de 10, para que con eso se realice la separación de dígitos
	exp = 1
	k += 1
	while max1/exp > 0: 
		countingSort(arr,exp)
		k += 1
		exp *= 10
#Arreglo para probar el algoritmo
arr = [1,10,100,1000,10000] 
print("Arreglo Original")
print(arr)
print("Arreglo Ordenado")
radixSort(arr) 
for i in range(len(arr)): 
	print(arr[i]),
print("")
print("Pasos: "+str(k))
"""
Puntos
n-k
0-3  1
1-4  10
2-5  100
3-6  1000
4-7  10000
5-8  100000
6-9
7-10
8-11
9-12
10-13
"""