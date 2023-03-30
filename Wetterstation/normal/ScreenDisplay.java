package normal;

class ScreenDisplay implements Observer {
    @Override
    public void update(float temp, float humid) {
        System.out.println("Screen Display - Temperature: " + temp + " Humidity: " + humid);
    }
}
