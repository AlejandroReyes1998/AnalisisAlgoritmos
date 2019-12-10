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
IMPLEMENTACIÓN DEL ALGORITMO MERGESORT
FECHA: 11/SEP/18
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
//Funcion Merge
void merge(int A[], int p, int q, int r) { 
    int i, j, k=0; 
    int n1 = q - p + 1; 
    int n2 = r - q;    
    int L[n1], R[n2];cont1++;
    for (i = 0; i < n1; i++){
        cont1++;
        L[i] = A[p + i];
    }         
    for (j = 0; j < n2; j++){
        R[j] = A[q + 1 + j]; cont1++;
    }    
    i = 0; 
    j = 0; cont1++;
    for(k=p; k<r+1; k++){
        if(i < n1 && j < n2){
            if (L[i] <= R[j]){
                A[k] = L[i];
                i++; cont1++;
            }
            else{
                A[k] = R[j];
                j++; cont1++;
            }
        }else if(i < n1){
            A[k] = L[i];
            i++; cont1++;
        }else if(j < n2){
            A[k] = R[j];
            j++; cont1++;
        }   
    }
}
//Funcion MergeSort, que a su vez se apoya de Merge para realizar el ordenamiento
void mergeSort(int A[], int p, int r){ 
     cont2++;
    if (p<r){ 
        int q = (p+r)/2; 
        mergeSort(A, p, q);  cont2++;
        mergeSort(A, q+1, r);  cont2++;
        merge(A, p, q, r);  cont2++;
    } 
} 

int main() {
//Arreglo inicial 
    int A[] = {9,5,3,6,2,4,2,5,3,1,4,3}; 
    //Obtenemos el tamaño del arreglo
    int A_TAM = sizeof(A)/sizeof(A[0]); 
    //Imprimimos arreglo original
    printf("Arreglo inicial \n"); 
    imprimir(A, A_TAM); 
    //ordenamos
    mergeSort(A, 0, A_TAM -1 ); 
    //imprimimos el arreglo ordenado
    printf("Arrelgo ordenado \n"); 
    imprimir(A, A_TAM); 
    //imprimimos contadores
    printf("Contador Merge: %d\n",cont1);
    printf("Contador MergeSort: %d\n",cont2);  
    return 0; 
} 
