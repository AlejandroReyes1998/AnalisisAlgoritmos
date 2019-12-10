# -*- coding: utf-8 -*-
"""
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
ANALISIS DE ALGORITMOS
GRUPO: 3CV1
ALUMNOS:
Reyes Valenzuela Alejandro
PROFESOR: BENJAMÍN LUNA BENOSO
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Implelentación de codificación-decodificación de Huffman
FECHA: 25/NOV/18
"""

from heapq import heappush, heappop, heapify
from collections import Counter,defaultdict
import sys

def leerfichero(path):
	#Permisos de lectura
	doc = open(path,"r").read()
	return doc[:len(doc)]

def frecuencias(array,count):
	#Encontramos las frecuencias del archivo
	doc = open("codificar/frecuencias.txt","w")
	for elem in array:
		element = elem[0]
		#Contamos las ocurrencias de los caracteres
		frecuency =  str(count[elem[0]])
		doc.write("%s | %s\n" %(element , frecuency))
	doc.close()

def codificacion(array):
	#COn base al caracter, encontramos el código correspondiente
	doc = open("codificar/codificacion.txt","w")
	for elem in array:
		element = elem[0]
		code = elem[1]
		doc.write("%s | %s\n" %(element , code))
	doc.close()

#Codifica el archivo
def codificaArchivo(array,string):
	for elem in array:
		string = string.replace(elem[0],str(elem[1]))
	doc = open("codificar/archivo_codificado.txt","w")
	doc.write(string)
	doc.close()
	return string

#Decodifica el archivo
def decodificaArchivo(dictionary, text):
	#Buscamos los caracteres en el diccionario
	res = ""
	while text:
		for k in dictionary:
			if text.startswith(k):
				res += dictionary[k]
				text = text[len(k):]
	doc = open("decodificar/archivo_decodificado.txt","w")
	doc.write(res)
	doc.close()

def huffman(dict_freq):
	#Mediante el uso de heap, determinamos las frecuencias de las palabras
	heap = [[wt, [sym, ""]] for sym, wt in dict_freq.items()]
	heapify(heap)
	while len(heap) > 1:
		#Con base al arbol generado recorremos para que funcione
		lo = heappop(heap)
		hi = heappop(heap)
		#Inserción de nodos
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
		#Regresamos la codificacion para el archivo
	return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def main():
	#Recuperamos la cadena original
	txt = leerfichero("original.txt")
	#Se usa la libreria collections para encontrar las frecuencias del archivo
	dict_freq = Counter(txt)
	#Con las frecuencias generamos el arbol
	huff = huffman(dict_freq)
	frecuencias(huff,dict_freq)
	#Generamos la codificacion
	codificacion(huff)
	#Codificacion
	codeado=codificaArchivo(huff,txt)
	print("archivo codificado!")
	#Pasamos la codificación de Huffman a diccionario para su decodificación
	dictofdicts = defaultdict(dict)
	for car, cod in huff:
		dictofdicts[cod] = car
	e=dict(dictofdicts)
	#Decodificacion
	decodificaArchivo(e,codeado)
	print("archivo decodificado")

if __name__ == '__main__':
	main()