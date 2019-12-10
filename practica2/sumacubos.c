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
IMPLEMENTACIÓN DEL ALGORITMO DE S DE MANERA RECURSIVA
FECHA: 1/SEP/18
*/
#include <stdio.h>
#include <stdlib.h>
int pasos=0;
//Implementaciön del algoritmo
int S(int n){
	int res;
	//Disminuimos n hasta obtener el 1
	if(n==1){pasos++;return 1;}
	else{
	//Le sumamos el cubo y seguimos disminuyendo
	pasos++;
	res=S(n-1)+(n*n*n);
	return res;	
	}
}


//MAIN
int main()
{
	int n;
	printf("Introduce un numero:");
	scanf("%d",&n);
	//Llamamos a la función
	printf("\nSuma:%d",S(n));
	//Imprimimos el valor de k
	printf("\nPasos:%d",pasos);
	return 0;
}
