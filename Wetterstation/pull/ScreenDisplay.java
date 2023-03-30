package pull;

public class ScreenDisplay implements Observer {
	private Subject subject;

	public ScreenDisplay(Subject subject) {
		this.subject = subject;
		subject.registerObserver(this);
	}

	@Override
	public void update() {
		float temperature = subject.getTemperature();
		float humidity = subject.getHumidity();
		System.out.println("Screen Display - Temperature: " + temperature + " Humidity: " + humidity);
	}
}