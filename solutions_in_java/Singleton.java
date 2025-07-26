public class Singleton {
    private static final Singleton INSTANCE = new Singleton();
    
    private Singleton() {
        // Private to prevent external instantiation
    }
    
    public static Singleton getInstance() {
        return INSTANCE;
    }
}