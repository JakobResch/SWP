import PizzaPackage.*;

public class HamburgPizzeria extends PizzaFactory{
    @Override
    protected Pizza createPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Salami")){
            pizza = new HamburgSalami();
        }
        else if(pizzaname.equals("Hawaii")){
            pizza = new HamburgHawaii();
        }
        else if(pizzaname.equals("Calzone")){
            pizza = new HamburgClazone();
        }
        else if(pizzaname.equals("Quattro Stationi")){
            pizza = new HamburgQuattroStationi();
        }
        else{
            System.out.println("Bitte gib eine der angebotenen Pizzen ein!");
        }

        return pizza;

    }
}
