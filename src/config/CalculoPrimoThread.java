package config;

public class CalculoPrimoThread extends Thread {

    private int limiteInferior, limiteSuperior;

    public CalculoPrimoThread(int limiteInferior, int limiteSuperior) {
        this.limiteInferior = limiteInferior;
        this.limiteSuperior = limiteSuperior;
        System.out.println("Computar primos (" + limiteInferior + ", " + limiteSuperior + ")");
    }

    public void run() {
        for (int i = limiteInferior; i < this.limiteSuperior; i++) {
            if(calculaPrimo(i)) System.out.println(i);
        }
    }

    public boolean calculaPrimo(int numero) {
        for (int divisor = 2; divisor < numero; divisor++) if (numero % divisor == 0) return false;
        return true;
    }
}
