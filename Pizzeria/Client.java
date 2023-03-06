import PizzaPackage.Pizza;
import java.util.Scanner;

public class Client{
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("In welcher Stadt bestellen Sie eine Pizza?(Hamburg, Rostock, Berlin, Lokal)");
        String stadt = scanner.nextLine();
        System.out.println("Welche Pizza möchten Sie bestellen? (Calzone, Salami, Hawaii, Quattro Stationi)");
        String Pizza = scanner.nextLine();

        if (stadt.equalsIgnoreCase("Berlin")) {
            if (Pizza.equalsIgnoreCase("Calzone")) {
                System.out.println("Eine Pizza Calzone in Berlin wird bestellt.");
                PizzaFactory pizzeriaBC = new BerlinPizzeria();
                Pizza pizzaBC = pizzeriaBC.newPizza("Calzone");
            }
            else if (Pizza.equalsIgnoreCase("Salami")) {
                System.out.println("Eine Pizza Salami in Berlin wird bestellt.");
                PizzaFactory pizzeriaBS = new BerlinPizzeria();
                Pizza pizzaBS = pizzeriaBS.newPizza("Salami");
            }
            else if (Pizza.equalsIgnoreCase("Hawaii")) {
                System.out.println("Eine Pizza Hawaii in Berlin wird bestellt..");
                PizzaFactory pizzeriaBH = new BerlinPizzeria();
                Pizza pizzaBH = pizzeriaBH.newPizza("Hawaii");
            }
            else if (Pizza.equalsIgnoreCase("Quattro Stationi")) {
                System.out.println("Eine Pizza Quattro Stationi in Berlin wird bestellt.");
                PizzaFactory pizzeriaBQ = new BerlinPizzeria();
                Pizza pizzaBQ = pizzeriaBQ.newPizza("Quattro Stationi");
            }else {
                System.out.println("Error: 401 unauthorized");
            }
        
        
        } else if (stadt.equalsIgnoreCase("Hamburg")) {
            if (Pizza.equalsIgnoreCase("Calzone")) {
                System.out.println("Eine Pizza Calzone in Hamburg wird bestellt.");
                PizzaFactory pizzeriaHC = new HamburgPizzeria();
                Pizza pizzaHC = pizzeriaHC.newPizza("Calzone");
            }
            else if (Pizza.equalsIgnoreCase("Salami")) {
                System.out.println("Eine Pizza Salami in Hamburg wird bestellt.");
                PizzaFactory pizzeriaBS = new HamburgPizzeria();
                Pizza pizzaHS = pizzeriaBS.newPizza("Salami");
            }
           else if (Pizza.equalsIgnoreCase("Hawaii")) {
                System.out.println("Eine Pizza Hawaii in Hamburg wird bestellt..");
                PizzaFactory pizzeriaBH = new HamburgPizzeria();
                Pizza pizzaHH = pizzeriaBH.newPizza("Hawaii");
            }
            else if (Pizza.equalsIgnoreCase("Quattro Stationi")) {
                System.out.println("Eine Pizza Quattro Stationi in Hamburg wird bestellt.");
                PizzaFactory pizzeriaBQ = new HamburgPizzeria();
                Pizza pizzaHQ = pizzeriaBQ.newPizza("Quattro Stationi");
            }else {
                System.out.println("Error: 401 unauthorized. ");
            }
        
        
        } else if (stadt.equalsIgnoreCase("Rostock")) {
            if (Pizza.equalsIgnoreCase("Calzone")) {
                System.out.println("Eine Pizza Calzone in Rostock wird bestellt.");
                PizzaFactory pizzeriaBC = new RostockPizzeria();
                Pizza pizzaRC = pizzeriaBC.newPizza("Calzone");
            }
            else if (Pizza.equalsIgnoreCase("Salami")) {
                System.out.println("Eine Pizza Salami in Rostock wird bestellt.");
                PizzaFactory pizzeriaBS = new RostockPizzeria();
                Pizza pizzaRS = pizzeriaBS.newPizza("Salami");
            }
            else if (Pizza.equalsIgnoreCase("Hawaii")) {
                System.out.println("Eine Pizza Hawaii in Rostock wird bestellt..");
                PizzaFactory pizzeriaBH = new RostockPizzeria();
                Pizza pizzaRH = pizzeriaBH.newPizza("Hawaii");
            }
           else if (Pizza.equalsIgnoreCase("Quattro Stationi")) {
                System.out.println("Eine Pizza Quattro Stationi in Rostock wird bestellt.");
                PizzaFactory pizzeriaBQ = new RostockPizzeria();
                Pizza pizzaRQ = pizzeriaBQ.newPizza("Quattro Stationi");
            }else {
                System.out.println("Error: 401 unauthorized. ");
            }
        }else if (stadt.equalsIgnoreCase("Lokal")) {
            if (Pizza.equalsIgnoreCase("Calzone")) {
                System.out.println("Eine Pizza Calzone wird bestellt.");
                PizzaFactory pizzeriaBC = new Pizzeria();
                Pizza pizzaC = pizzeriaBC.newPizza("Calzone");
            }
            else if (Pizza.equalsIgnoreCase("Salami")) {
                System.out.println("Eine Pizza Salami wird bestellt.");
                PizzaFactory pizzeriaBS = new Pizzeria();
                Pizza pizzaS = pizzeriaBS.newPizza("Salami");
            }
            else if (Pizza.equalsIgnoreCase("Hawaii")) {
                System.out.println("Eine Pizza Hawaii wird bestellt..");
                PizzaFactory pizzeriaBH = new Pizzeria();
                Pizza pizzaBH = pizzeriaBH.newPizza("Hawaii");
            }
            else if (Pizza.equalsIgnoreCase("Quattro Stationi")) {
                System.out.println("Eine Pizza Quattro Stationi wird bestellt.");
                PizzaFactory pizzeriaBQ = new Pizzeria();
                Pizza pizzaQ = pizzeriaBQ.newPizza("Quattro Stationi");
            }else {
                System.out.println("Error: 401 unauthorized.");
        }
    }else {
            System.out.println("Error: 401 unauthorized.");
        
        }
        
    
}}
