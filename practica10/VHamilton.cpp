/*
'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
ANALISIS DE ALGORITMOS
GRUPO: 3CV1
ALUMNOS:
Gutierrez Povedano Pablo
Reyes Valenzuela Alejandro
PROFESOR: BENJAMÍN LUNA BENOSO
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IMPLEMENTACIÓN DEL ALGORITMO DEL CICLO HAMILTONIANO
FECHA: 3/DIC/18
'''
*/
#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string.h>
int k=0;
int tam=0;
char bufer[1000];
char bufer2[1000];
//Leemos el grafo con las rutas que puede tomar desde determiano nodo
char*  leerGrafo()
{	
   	FILE *pfile;   	
   	int cont=0;
   	pfile = fopen("grafo.txt","r");
  	if (!pfile)
   	{
   		return "error";
   	}

   	while(fgets(bufer,1000, pfile)!=NULL)
   	{
 //     	printf("%s",bufer);      	
   	}

	for(int i=0;i<=strlen(bufer);i++)
	{
		if(bufer[i]==','){cont=i; break;}
	}
	tam=cont;  	
  	fclose(pfile);
   	return bufer;	
}
//Leemos el certificado para obtener la ruta de verificación
char* leerCertificado()
{
	FILE *pfile;   
   	pfile = fopen("certificado.txt","r");
  	if (!pfile)
   	{
   		return NULL;
   	}

   	while(fgets(bufer2,1000, pfile)!=NULL)
   	{
 //     	printf("\n%s",bufer2);      	
   	}	
  	
  	fclose(pfile);  
   	return bufer2;
}

int main()
{
	//Obtenemos el grafo y el certificado de los archivos
	leerGrafo();
	leerCertificado();	
	int matriz[tam][tam];	
	int l=0,i=0,j=0,longitud=0,cont=0;
	longitud=strlen(bufer);
	//Impresión del grafo y del certificado
	printf("\ngrafo:%s",bufer);
	printf("\nCertificado:%s",bufer2);
	int vertices[tam+1];
	//Certificado
	for(int i=0;i<strlen(bufer2);i++)
	{		
		if(bufer2[i]==','){cont++;}
		else{vertices[cont]=((int)bufer2[i])-48;}
	}
	cont++;	
	/*
	el grafo se representa con una matriz nxn donde cada arreglo 
	representa un vertice con 1 si tiene unión con otro vértice y 0 si no tiene.
	*/
	while(l<longitud)
	{
		if(bufer[l]==',')
		{
			i++;
			j=0;
		}
		else
		{
			matriz[i][j]=((int)bufer[l])-48;			
			j++;
		}
	l++;
	}
	//Si el grafo no tiene conexiones no es un ciclo
	if(cont<tam+1||cont>tam+1){printf("\nNo es un ciclo"); return 0;}
	int cu=0;
	int ne=0;
	int noes=0;
	int ini=vertices[0];
	//El algoritmo como tal
	for(int i=0;i<tam;i++)
	{
        k++;
		cu=vertices[i]-1;
		ne=vertices[i+1]-1;
	//Verificamos que sea posible realizar el trayecto dado el grafo 
		if(matriz[cu][ne]==1)
		{
			for (int j = 0; j < tam; j++)
			{
				//Si se pudo realizar el trayecto completo (el ciclo)
				matriz[j][ne]=0;
                k++;
			}
		}
		else
		{
			//No se pudo por algún motivo
			noes=1;
			break;
		}
	}
	//Impresión de resultados
	if(noes==0)
	{
		printf("\nEs un ciclo\n");
	}
	else
	{
		printf("\nNo es un ciclo\n");
	}	
	printf("Contador :%d",k);
	return 0;
}


