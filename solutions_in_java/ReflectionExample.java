import java.lang.reflect.Method;

public class ReflectionExample {
    public static void main(String[] args) throws Exception {
        String str = "Hello";
        Method method = String.class.getMethod("length");
        int length = (int) method.invoke(str);
        System.out.println(length);  // Outputs: 5
    }
}