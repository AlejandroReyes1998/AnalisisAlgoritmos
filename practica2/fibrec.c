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
IMPLEMENTACIÓN DEL ALGORITMO DE FIBONACCI DE MANERA RECURSIVA
FECHA: 1/SEP/18
*/
#include <stdio.h>
//Contador
extern int k = 0;
int Fibonacci(int x);
int main()
{
  int n;
 //Pedimos el n-ésimo término de la sucesión
  printf("Termino de la sucesión?\n");
  scanf("%d", &n);
 //Imprimimos el término
  printf("El término %d de la sucesión de Fibonacci es:%d\n", n,Fibonacci(n));
  printf("k=%d\n",k);
  return 0;
}
int Fibonacci(int x){
  if(x==0||x==1)
  {
    //0 o 1 significa que hemos terminado
  	k++;
  	return 1;
  }  
  else{
    //Seguimos disminuyendo el valor hasta llegar a 0 o 1
  	k++;
  	return Fibonacci(x-1) + Fibonacci(x-2); 
  }  
}