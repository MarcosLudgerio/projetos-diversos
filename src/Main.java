import config.MinhaThread;

public class Main {
    public static void main(String[] args) {
       int start = 1;
       int end = 1000000;
        for (int i = start; i < end; i++) {
            if(calculaPrimo(i)) System.out.println(i);
        }
    }

    public static boolean calculaPrimo(int numero) {
        for (int divisor = 2; divisor < numero; divisor++) if (numero % divisor == 0) return false;
        return true;
    }
}