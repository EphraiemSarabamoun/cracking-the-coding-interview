import java.util.*;
import java.util.function.Supplier;

class User {
    String name;
    int tier;
    User(String n, int t) { name = n; tier = t; }
}

public class WeightedRandom {
    public static Supplier<User> weightedSampler(List<User> users) {
        int total = users.stream().mapToInt(u -> u.tier).sum();
        List<Integer> cum = new ArrayList<>();
        int sum = 0;
        for (User u : users) {
            sum += u.tier;
            cum.add(sum);
        }
        return () -> {
            int rand = new Random().nextInt(total);
            int idx = Collections.binarySearch(cum, rand + 1);
            if (idx < 0) idx = -idx - 1;
            return users.get(idx);
        };
    }

    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("A", 1), new User("B", 2));
        Supplier<User> sampler = weightedSampler(users);
        System.out.println(sampler.get().name); 
    }
}