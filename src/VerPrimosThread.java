import config.CalculoPrimoThread;

public class VerPrimosThread {
    public static void main(String[] args) {
        int start = 1;
        int end = 1000000;
        CalculoPrimoThread thread = new CalculoPrimoThread(start, end);
        thread.start();

    }
}
