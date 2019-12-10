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
IMPLEMENTACIÓN DEL ALGORITMO QUICKSORT
FECHA: 13/SEP/18
*/
#include<stdlib.h> 
#include<stdio.h>
extern int cont1 = 0;
extern int cont2 = 0;
//Funcion que imprime arreglos
void imprimir(int A[], int TAM) { 
    int i; 
    for (i=0; i < TAM; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
}
/*Función que intercambia el valor de dos variables
para ello utilizamos apuntadores para que las funciones trabajen con los valores actualizados*/
void exchange(int* a, int* b) { 
    int aux=*a;
    *a=*b;
    *b=aux;
}
//Algoritmo Partition
int Partition(int A[],int p,int r){
	int x=A[r];cont1++;
	int i=p-1;cont1++;
	int j=p;cont1++;
	for(j;j<=r-1;j++){
		if(A[j]<=x){
			i++;cont1++;
			exchange(&A[i],&A[j]);cont1++;
		}
	}
	exchange(&A[i+1],&A[r]);cont1++;
	return i+1;
}
//Algoritmo QuickSort, que se apoya de Partition
void QuickSort(int A[],int p,int r){
	cont2++;
    int q;
	if(p < r){
		q=Partition(A,p,r);cont2++;
		QuickSort(A,p,q-1);cont2++;
		QuickSort(A,q+1,r);cont2++;

	}  
}
int main() {
//Arreglo inicial 
    int A[] = {13,10,9,8,7,5,4,3,2,1};
    //{13,10,9,8,7,5,4,3,2,1};   
    //Obtenemos el tamaño del arreglo
    int A_TAM = sizeof(A)/sizeof(A[0]); 
    printf("Tamaño del Arreglo:%d\n",A_TAM);
    //Imprimimos arreglo original
    printf("Arreglo inicial \n"); 
    imprimir(A, A_TAM); 
    //ordenamos
    QuickSort(A, 0, A_TAM -1 ); 
    //imprimimos el arreglo ordenado
    printf("Arrelgo ordenado \n"); 
    imprimir(A, A_TAM); 
    //imprimimos contadores
    printf("Contador Partition: %d\n",cont1);
    printf("Contador Quicksort: %d\n",cont2);  
    return 0; 
} 
