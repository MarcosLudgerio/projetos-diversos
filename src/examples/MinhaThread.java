package examples;

public class MinhaThread extends Thread {

    int[][] matrizA, matrizB;

    public MinhaThread(int[][] matrizA, int[][] matrizB) {
        this.matrizA = matrizA;
        this.matrizB = matrizB;
    }

    public void run() {
        calculaMultiplicacaoMatriz(this.matrizA, this.matrizB);
    }

    public int[][] calculaMultiplicacaoMatriz(int[][] matrizA, int[][] matrizB) {
        int linhaA = matrizA.length;
        int linhaB = matrizB.length;
        int colunaA = matrizA[0].length;
        int colunaB = matrizB[0].length;


        if (colunaA != linhaB) {
            System.out.println("Impossível multiplicar");
            return null;
        }

        int[][] matrizC = new int[linhaA][colunaB];

        for (int i = 0; i < linhaA; i++) {
            for (int j = 0; j < colunaB; j++) {
                matrizC[i][j] = 0;
                for (int k = 0; k < colunaA; k++) {
                    matrizC[i][j] += matrizA[i][k] * matrizB[k][j];
                }
            }
        }
        return matrizC;
    }
}
