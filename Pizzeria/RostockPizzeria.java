import PizzaPackage.*;

public class RostockPizzeria extends PizzaFactory{
    @Override
    protected Pizza createPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Salami")){
            pizza = new RostockSalami();
        }
        else if(pizzaname.equals("Hawaii")){
            pizza = new RostockHawaii();
        }
        else if(pizzaname.equals("Calzone")){
            pizza = new RostockCalzone();
        }
        else if(pizzaname.equals("Quattro Stationi")){
            pizza = new RostockQuattroStationi();
        }
        else{
            System.out.println("Bitte gib eine der angebotenen Pizzen ein!");
        }

        return pizza;

    }
}
