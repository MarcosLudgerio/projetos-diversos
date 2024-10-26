import examples.MinhaThread;

public class Main {
    public static void main(String[] args) {
        int[][] matriz1 = {
                {1, 2, 3},
                {4, 5, 6}
        };
        int[][] matriz2 = {
                {7, 8},
                {9, 10},
                {11, 12}
        };
        MinhaThread thread = new MinhaThread(matriz1, matriz2);
        thread.start();
    }
}