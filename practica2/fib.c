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
IMPLEMENTACIÓN DEL ALGORITMO DE FIBONACCI DE MANERA ITERATIVA
FECHA: 1/SEP/18
*/
#include <stdio.h>
int Fibonacci(int x);
int main()
{
  int n;
 
  printf("Termino de la sucesión?\n");
  scanf("%d", &n);
 
  printf("El término %d de la sucesión de Fibonacci es:%d\n", n,Fibonacci(n));
 
  return 0;
}
int Fibonacci(int x){
  //Definimos los primeros dos terminos de la sucesión (0 y 1), una variable auxiliar y el contador
  int ter1 = 0, ter2 = 1, sig, i,k=0;
  for (i = 0; i < x; i++,k++)
  {  //Sumamos los términos 1 y 2, los asignamos la suma a la variable auxiliar y reasignamos los valores de los términos a sumar
      sig = ter1 + ter2;k++;
      ter1 = ter2;k++;
      ter2 = sig;k++;
  }
  printf("k=%d\n",k);
  return sig;
}