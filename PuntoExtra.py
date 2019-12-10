'''Tabla hash donde guardaremos los valores, como llave usaremos el valor del 
arreglo y como valor de la llave usaremos el índice del for
'''
tabla={}
def suma(A,sumx):
	#Arreglo donde guardamos los índices que dan la suma requerida
	num=[]
	#Bandera que nos dice si existen los números o no
	flag=None
	#Variable que nos dice el número de valores que cumplen con la suma
	val=0
	#Guardamos en la tabla hash como llave usaremos el valor del arreglo y como valor de la llave usaremos el índice del for
	for i in range(0,len(A)):
		tabla[A[i]] = i
	for i in range(0,len(A)):
		#Buscamos el valor en la tabla hash, si al hacer la resta
		#del valor buscado con otro valor del arreglo, existe su complemento en la tabla, encotramos los pares
		a=tabla.get(sumx - A[i],i)
		if (a!= i):
			#Si el valor existe (y no es el mismo :v)
			#Encontramos el valor y por ende,aumentamos contadores y registramos valores
			flag=True
			val=val+1
			#Evitamos duplicados en el vector solución
			if a not in num:
				num.append(a)
	#Existe(n) valores que dan la suma
	if(flag):
		#Impresión de valores
		print("Números en el arreglo que sumen "+str(sumx)+":")
		for i in range(0,len(num)):
			print(A[num[i]])
			if((i+1)%2==0):
				print("-------------")
	#Pues no existen :v
	else:
		print("No existen números en el arreglo que sumen "+str(sumx))

def main():
	A = [-14,16,29,1,12,-15,0,-16,2,28,28,300,16,3]
	sumx=4
	print("Valores Arreglo")
	print(A)
	print("Valor a encontrar mediante suma: "+str(sumx))
	suma(A,sumx)


if __name__ == '__main__':
	main()