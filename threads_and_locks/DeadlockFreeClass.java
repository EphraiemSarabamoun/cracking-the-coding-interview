public class DeadlockFreeClass {
    private final Object lock1 = new Object();
    private final Object lock2 = new Object();

    public boolean acquireLocks() {
        // Always lock1 then lock2 (hierarchy)
        synchronized (lock1) {
            synchronized (lock2) {
                // Do work
                return true;
            }
        }
    }
}
