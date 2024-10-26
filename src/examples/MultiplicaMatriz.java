package examples;

public class MultiplicaMatriz extends Thread {
    // Para que seja possível a multiplicação de duas matrizes, as condições precisam ser atendidas:
    // 1. O número de colunas da primeira matrz tem que ser igual ao número de linhas da segunda
    /* "o resultado da multiplicação é uma matriz que possui
        o mesmo número de linhas da primeira matriz e o mesmo número de colunas da segunda matriz.
    * A = [[1,3],[7,9],[4,6]]
    * B = [[9,5,3],[1,8,9]]    *
    * A x B = [[12,29,30],[72,107,102],[42,68,66]]
    *
    */
    public static void main(String[] args) {

        int[][] matrizA = new int[2][2];
        int[][] matrizB = new int[2][5];

        matrizA[0][0] = 1;
        matrizA[0][1] = 13;
        matrizA[1][0] = 7;
        matrizA[1][1] = 9;
        matrizA[2][0] = 4;
        matrizA[2][1] = 6;

        matrizB[0][0] = 5;
        matrizB[0][1] = 8;
        matrizB[0][2] = 3;
        matrizB[1][0] = 10;
        matrizB[1][1] = 2;
        matrizB[1][2] = 11;



        if(matrizA.length != matrizB[1].length) System.out.println("Impossível multiplicar");

        int[][] matrizC = new int[matrizA.length][matrizB[1].length];



        for (int i = 0; i < matrizA.length; i++) {
            for (int j = 0; j < matrizB[1].length; j++) {
                // C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
                // C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
                // C[0][2] = A[0][0] * B[0][2] + A[0][1] * B[1][2]

                // C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
                // C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
                // C[1][2] = A[1][0] * B[0][2] + A[1][1] * B[1][2]

                // C[2][0] = A[2][0] * B[0][0] + A[2][1] * B[1][0]
                // C[2][1] = A[2][0] * B[0][1] + A[2][1] * B[1][1]
                // C[2][2] = A[2][0] * B[0][2] + A[2][1] * B[1][2]
                matrizC[i][j] = matrizA[i][0] * matrizB[0][j] + matrizA[i][1] * matrizB[1][j];
            }
        }
        


    }


}
