package push;

class LEDDisplay implements Observer {
	@Override
	public void update(float temperature, float humidity) {
		if (temperature >= 30) {
			System.out.println("LEDDisplay - Temperature high: Red signal");
		} else if (temperature <= 10) {
			System.out.println("LEDDisplay - Temperature low: Blue signal");
		} else {
			System.out.println("LEDDisplay - Temperature normal: Green signal");
		}
	}
}
