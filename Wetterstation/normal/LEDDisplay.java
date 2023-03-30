package normal;

class LEDDisplay implements Observer {
    @Override
    public void update(float temp, float humid) {
        if (temp >= 30) {
            System.out.println("LEDDisplay - Temperature high: Red signal");
        } else if (temp <= 10) {
            System.out.println("LEDDisplay - Temperature low: Blue signal");
        } else {
            System.out.println("LEDDisplay - Temperature normal: Green signal");
        }
    }
}
