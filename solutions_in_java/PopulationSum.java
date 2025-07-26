import java.util.ArrayList;
import java.util.List;


class Country {
    private String continent;
    private int population;

    public Country(String continent, int population) {
        this.continent = continent;
        this.population = population;
    }

    public String getContinent() {
        return continent;
    }

    public int getPopulation() {
        return population;
    }
}

public class PopulationSum {

    public static int sumPopulationNoLambda(List<Country> countries, String continent) {
        int sum = 0;
        for (Country country : countries) {
            if (country.getContinent().equalsIgnoreCase(continent)) {
                sum += country.getPopulation();
            }
        }
        return sum;
    }

    public static int sumPopulationWithLambda(List<Country> countries, String continent) {
        return countries.stream()
                .filter(country -> country.getContinent().equalsIgnoreCase(continent))
                .mapToInt(Country::getPopulation)
                .sum();
    }

    public static void main(String[] args) {
        List<Country> countries = new ArrayList<>();
        countries.add(new Country("Asia", 1400));    // China
        countries.add(new Country("Asia", 1380));    // India
        countries.add(new Country("Europe", 83));    // Germany
        countries.add(new Country("Europe", 67));    // France
        countries.add(new Country("Africa", 206));   // Nigeria
        countries.add(new Country("Africa", 59));    // South Africa
        countries.add(new Country("North America", 331)); // USA

        String targetContinent = "Asia";

        int sumNoLambda = sumPopulationNoLambda(countries, targetContinent);
        System.out.println("Sum of populations in " + targetContinent + " (no lambda): " + sumNoLambda + " million");

        int sumWithLambda = sumPopulationWithLambda(countries, targetContinent);
        System.out.println("Sum of populations in " + targetContinent + " (with lambda): " + sumWithLambda + " million");
    }
}