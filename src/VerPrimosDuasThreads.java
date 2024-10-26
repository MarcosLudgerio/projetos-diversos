import examples.CalculoPrimoThread;

public class VerPrimosDuasThreads {
    public static void main(String[] args) {
        int start = 1;
        int end = 1000000;
        CalculoPrimoThread thread = new CalculoPrimoThread(start, end /2);
        thread.start();

        CalculoPrimoThread thread2 = new CalculoPrimoThread((end /2) + 1, end);
        thread2.start();
    }
}
