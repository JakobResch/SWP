package push;

public class ScreenDisplay implements Observer {
	@Override
	public void update(float temperature, float humidity) {
		System.out.println("Screen Display - Temperature: " + temperature + " Humidity: " + humidity);
	}
}