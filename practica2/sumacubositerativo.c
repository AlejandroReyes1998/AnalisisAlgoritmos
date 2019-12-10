/*
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
ANALISIS DE ALGORITMOS
GRUPO: 3CV1
ALUMNOS:
Gutierrez Povedano Pablo
Reyes Valenzuela Alejandro
PROFESOR: BENJAMÍN LUNA BENOSO
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IMPLEMENTACIÓN DEL ALGORITMO DE S DE MANERA ITERATIVA
*/
#include <stdio.h>
#include <stdlib.h>

int pasos=0;

int s(int n){
	int acum=0;
	pasos++;
	for(int x=1;x<=n;x++){
		//sumamos los cubos y los asignamos a una variable que almacenará la suma total
		pasos++;
		acum=acum+(x*x*x);
	}
	return acum;
}


int main()
{
	int n;
	printf("Introduce un numero:");
	scanf("%d",&n);	
	//Llamamos a la función
	printf("\nSuma:%d",s(n));
	//Imprimimos el valor de k
	printf("\nPasos:%d",pasos);
	return 0;
}