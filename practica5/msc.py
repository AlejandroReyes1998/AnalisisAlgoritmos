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
IMPLEMENTACIÓN DEL ALGORITMO DE MAXIMO SUBARREGLO Y MAXIMO SUBARREGLO CRUZADO, TANTO CON RECURSIÓN COMO
POR FUERZA BRUTA
FECHA: 30/SEP/18
'''
#MAXSUB - MAXSUBCRUZ - MSFB
k =0
l=0
m=0
#Maximo subarreglo cruzado
def MaxSubCruz(A, bajo, mitad, alto):
	#COntador
	global l
	#Infinito
	suma_izq = -10000
	suma = max_der = max_izq = 0
	#Busqueda de la suma por la izquierda
	for i in range(mitad, bajo+1, -1):
		l += 1 
		suma = suma + A[i]
		if suma >= suma_izq:
			l += 1
			suma_izq = suma
			max_izq = i
	#Infinito 2 y reinicio de suma total
	suma_der = -10000
	suma = 0
	#Busqueda por la derecha
	for i in range(mitad+1, alto+1):
		l += 1
		suma = suma + A[i]
		if suma >= suma_der:
			l += 1
			suma_der = suma
			max_der = i
	#Regresamos los valores que nuestras búsquedas arrojaron
	return (max_izq, max_der, suma_der + suma_izq)
#Maximo subarreglo general
def MaxSub(A,bajo,alto):
	global k
	#Solo hay un elemento
	if alto == bajo:
		k += 1
		return (bajo, alto, A[bajo])
	else:
		#Buscamos los elementos por todo el arreglo
		mitad = int((alto+bajo)/2)
		#Recursividad para hallarlos en los extremos
		k += 1
		(bajo_izq, alto_izq, suma_izq) = MaxSub(A, bajo, mitad)
		k += 1
		(bajo_der, alto_der, suma_der) = MaxSub(A, mitad+1, alto)
		#Llamamos al cruzado en caso de que cruce por la mitad
		k += 1
		(bajo_cruz, alto_cruz, suma_cruz) = MaxSubCruz(A, bajo, mitad, alto)
	#Retornamos el valor donde se encuentre la suma (rango y suma)
	if suma_der >= suma_izq and suma_der >= suma_cruz:
		k += 1
		return (bajo_der, alto_der, suma_der)
	else:
		if suma_izq >= suma_der and suma_izq >= suma_cruz:
			k += 1
			return (bajo_izq, alto_izq, suma_izq)
		else:
			k += 1
			return (bajo_cruz, alto_cruz, suma_cruz)
#Implementación por fuerza bruta
def MSFB(A,bajo,alto):
	global m
	#infinito
	max_izq = max_der = 0
	suma_max = -10000
	for i in range(0,alto):
		m+=1
		suma = 0
		#Buscamos en ambos lados  del arreglo al mismo tiempo
		for j in range(i,alto):
			m+=1
			suma += A[j]
			if suma >= suma_max:
				m+=1
				suma_max = suma
				max_izq = i
				max_der = j
	return (max_izq, max_der, suma_max)
#Ejecuta Algoritmo Original
def main1():
	#[-2, 1, -3, 4, -1, 2, 1, -5, 4]
	A=[]
	tam=50
	for i in range(0,tam):
		A.append(randint(-20,20))
	print("Arreglo original")
	print(A)
	res=MaxSub(A,0,len(A)-1)
	print("Resultados:")
	print("Inicio Suma Max: "+str(res[0]))
	print("Alto Suma Max: "+str(res[1]))
	print("Suma Max: "+str(res[2]))
	print("MS: "+str(l))
	print("MSC: "+str(k))
#Ejecuta algoritmo por fuerza bruta
def main2():
	A=[]
	tam=45
	for i in range(0,tam):
		A.append(randint(-20,20))
	print("Arreglo original")
	print(A)
	res=MSFB(A,0,len(A)-1)
	print("Resultados:")
	print("Inicio Suma Max: "+str(res[0]))
	print("Alto Suma Max: "+str(res[1]))
	print("Suma Max: "+str(res[2]))
	print("MSFB: "+str(m))
main1()
main2()