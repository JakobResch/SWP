import PizzaPackage.*;

public class BerlinPizzeria extends PizzaFactory{

    @Override
    protected Pizza createPizza (String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Calzone")){
            pizza = new BerlinCalzone();
        }
        else if(pizzaname.equals("Hawaii")){
            pizza = new BerlinHawaii();
        }
        else if(pizzaname.equals("Calzone")){
            pizza = new BerlinCalzone();
        }
        else if(pizzaname.equals("Quattro Stationi")){
            pizza = new BerlinQuattroStationi();
        }
        else{
            System.out.println("Bitte gib eine der angebotenen Pizzen ein!");
        }

        return pizza;
    
    }


}
