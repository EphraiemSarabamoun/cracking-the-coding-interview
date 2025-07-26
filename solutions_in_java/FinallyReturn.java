public class FinallyReturn {
    public static int test() {
        try {
            return 1;  // This return is prepared but delayed
        } finally {
            System.out.println("Finally executes");  // Prints before return
        }
    }

    public static void main(String[] args) {
        System.out.println(test());  // Outputs: Finally executes \n 1
    }
}