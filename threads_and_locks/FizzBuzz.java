
public class FizzBuzz {
    private int n;
    private int current = 1;
    private final Object lock = new Object();

    public FizzBuzz(int n) {
        this.n = n;
    }

    public void fizz(Runnable printFizz) throws InterruptedException {
        while (true) {
            synchronized (lock) {
                if (current > n) return;
                if (current % 3 == 0 && current % 5 != 0) {
                    printFizz.run();
                    current++;
                    lock.notifyAll();
                } else {
                    lock.wait();
                }
            }
        }
    }
}
