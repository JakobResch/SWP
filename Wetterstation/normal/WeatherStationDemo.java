package normal;

public class WeatherStationDemo {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        ScreenDisplay screenDisplay = new ScreenDisplay();
        LEDDisplay ledDisplay = new LEDDisplay();

        weatherData.registerObserver(screenDisplay);
        weatherData.registerObserver(ledDisplay);

        weatherData.setMeasurements(25, 50);
        weatherData.setMeasurements(35, 60);

        weatherData.removeObserver(screenDisplay);

        weatherData.setMeasurements(5, 70);
    }
}
