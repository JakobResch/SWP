import PizzaPackage.Pizza;

public abstract class PizzaFactory{

    public Pizza newPizza(String pizzaname){

        Pizza pizza = createPizza(pizzaname);
        pizza.bake();
        pizza.cut();
        pizza.wrapUp();
        return pizza;
    }

    protected abstract Pizza createPizza(String pizzaname);

}
