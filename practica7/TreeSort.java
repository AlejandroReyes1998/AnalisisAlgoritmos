package treesort;

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
IMPLEMENTACIÓN DEL ALGORITMO DE TREE SORT
FECHA: 15/OCT/18
 */
class TreeSort {
    int k=0;

    //Declaramos nuestra estructura árbol con sus respectivos nodos
    class Nodo {

        int num;
        Nodo izq, der;

        public Nodo(int item) {
            num = item;
            izq = der = null;
        }
    }
    Nodo raiz;

    // Constructor 
    TreeSort() {
        raiz = null;
    }

    //Insertamos el valor del arreglo a la raiz
    void inserta(int num) {
        k++;
        raiz = insertaRec(raiz, num);
    }

    //Inserta un número en cierto nodo que le demos (dado un nodo de referencia
    Nodo insertaRec(Nodo raiz, int num) {
        /* Si el árbol está vacío regresamos un nuevo nodo*/
        if (raiz == null) {
            raiz = new Nodo(num);
            k++;
            return raiz;
            
        }
        /*Si el valor a insertar es mayor al que tenemos, lo mandamos
        a la derecha, en caso contrario lo mandamos a la izquierda*/
        if (num < raiz.num) {
            raiz.izq = insertaRec(raiz.izq, num);
            k++;
        } else if (num > raiz.num) {
            raiz.der = insertaRec(raiz.der, num);
            k++;
        }

        /* Retornamos el nodo raíz al que fue asignado el número*/
        return raiz;
    }

    //Recorrido inorden
    void inorordenRec(Nodo raiz) {
        if (raiz != null) {
            inorordenRec(raiz.izq);k++;
            System.out.print(raiz.num + " ");
            inorordenRec(raiz.der);k++;
        }
    }

    //Generamos el arbol dado un arreglo
    void insertaArreglo(int A[]) {
        for (int i = 0; i < A.length; i++) {
            inserta(A[i]);
            k++;
        }

    }

    //Función que imprime un arreglo
    void imprime(int A[]) {
        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i] + " ");
        }
    }

    public static void main(String[] args) {
        //Para poder usar los métodos de la clase
        TreeSort tree = new TreeSort();
        int A[] = {5, 4, 7, 2, 11, 1, 24, 112, 3};
        System.out.println("---ARREGLO ORIGINAL---");
        tree.imprime(A);
        System.out.println("");
        //Mandamos el arreglo para procesarlo como árbol y poder ordenarlo
        tree.insertaArreglo(A);
        //El arreglo ya fue ordenado
        System.out.println("---ARREGLO ORDENADO---");
        tree.inorordenRec(tree.raiz);
        System.out.println("");
        System.out.println("Pasos: "+tree.k);
    }
}
/*
Mejor caso
n-k
1-5
2-11
3-18
4-26
5-35
6-45
7-56
8-68
9-81
10-95
Peor caso
1-7
2-26
3-42
4-54
5-74
6-93
7-122
8-140
9-162
10-180
*/