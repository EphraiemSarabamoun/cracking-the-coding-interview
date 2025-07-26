import java.util.concurrent.locks.Lock;

class Philosopher extends Thread {
    private Lock leftFork, rightFork;
    private int id;

    public Philosopher(int id, Lock left, Lock right) {
        this.id = id;
        this.leftFork = left;
        this.rightFork = right;
    }

    private void think() { /* sleep */ }
    private void eat() { /* sleep */ }

    public void run() {
        while (true) {
            think();
            // Hierarchy: Lock lower ID fork first
            Lock first = (id < (id + 1) % 5) ? leftFork : rightFork;
            Lock second = (first == leftFork) ? rightFork : leftFork;
            first.lock();
            try {
                second.lock();
                try {
                    eat();
                } finally {
                    second.unlock();
                }
            } finally {
                first.unlock();
            }
        }
    }
}