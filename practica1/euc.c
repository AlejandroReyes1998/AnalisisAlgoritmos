/*Reyes Valenzuela Alejandro
Gutierrez Povedano Pablo
3CV1*/
#include <stdio.h>
#include <stdlib.h>
int euc(int m,int n);
int main(void){
	//Pedimos valores de m y n para calcular el MCD
	int m=0,n=0;
	printf("el MCD DE m:%d y n:%d es:%d\n",m,n,euc(m,n));
}
int euc(int m,int n){
	//Implementación del algoritmo de Euclides
	int r=0,k=0;
	while (n!= 0){
		r=m%n;k++;
		m=n;k++;
		n=r;k++;
	}
	printf("k=%d\n",k);
	return m;
}
