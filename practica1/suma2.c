/*Reyes Valenzuela Alejandro
Gutierrez Povedano Pablo
3CV1*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void suma(int C[],int B[],int TAM);
int main(void){
	printf("n=?\n");
	int TAM;
	scanf("%d",&TAM);
	int A[TAM];
	int B[TAM];
	time_t t;
	srand((unsigned) time(&t));
	int i=0;
	//Llenamos ambas matrices con 1's y 0's
	for(i=0;i<TAM;i++){
		A[i]=rand() % 2;
		B[i]=rand() % 2;
	}
	i=0;
	//Imprimimos ambos arreglos
	printf("Arreglo A\n");
	while(i<TAM){
		 printf("%d", A[i]);
		 i++;
	}
	i=0;
	printf("\n");
	printf("Arreglo B\n");
	while(i<TAM){
		printf("%d", B[i]);
		i++;
	}
	i=0;
	printf("\n");
	suma(A,B,TAM);
}
void suma(int A[],int B[],int TAM){
	int k=0,i=0,aux=0;
	int C[TAM+1];
	for(i = TAM-1;i>=0;i--,k++){
	//SUma de 0+0
	if(A[i]==0 && B[i]==0 && aux==0){
		C[i] = 0;k++;
		aux = 0;k++;	
	}
	//0+0 con acarreo
	else if(A[i]==0 && B[i]==0 && aux==1){
        C[i] = 1;k++;
        aux = 0;k++;
    }
    //1+0/0+1 sin acarreo
	else if(((A[i]==1 && B[i]==0)||(A[i]==0 && B[i]==1)) && aux==0){
		C[i] = 1;k++;
		aux = 0;k++;
	}
	//1+0/0+1 con acarreo
	else if(((A[i]==1 && B[i]==0)||(A[i]==0 && B[i]==1)) && aux==1){
        C[i] = 0;k++;
        aux = 1;k++;
    }
    //1+1 sin acarreo
	else if(A[i]==1 && B[i]==1 && aux==0){
		C[i] = 0;k++;
		aux = 1;k++;
	}
	//1+1 con acarreo
	else if(A[i]==1 && B[i]==1 && aux==1){
          C[i] = 1;k++;
          aux = 1;k++;
     	}
	}
	//Finalmente imprimimos el resultado, como el algoritmo terminó, dejamos de aumentar k.
	printf("Arreglo C (La suma de A Y B)\n");
	for(i=0;i<TAM;i++){
		printf("%d",C[i]);
	}
	printf("\n");
	printf("n=%d, k=%d\n",TAM,k);		
}
/*

*/
