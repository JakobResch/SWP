import PizzaPackage.Calzone;
import PizzaPackage.Hawaii;
import PizzaPackage.Pizza;
import PizzaPackage.QuattroStationi;
import PizzaPackage.Salami;

public class Pizzeria extends PizzaFactory{
    
    @Override
    protected Pizza createPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Calzone")){
            pizza = new Calzone();
        }
        else if(pizzaname.equals("Salami")){
            pizza = new Salami();
        }
        else if(pizzaname.equals("Hawaii")){
            pizza = new Hawaii();
        }
        else if(pizzaname.equals("Quattro Stationi")){
            pizza = new QuattroStationi();
        }
        else{
            System.out.println("Bitte gib eine der angebotenen Pizzen ein!");
        }

        return pizza;

    }
    
}
