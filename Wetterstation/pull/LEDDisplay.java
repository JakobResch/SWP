package pull;

class LEDDisplay implements Observer {
	private Subject subject;

	public LEDDisplay(Subject subject) {
        this.subject = subject;
        subject.registerObserver(this);
    }

	@Override
    public void update() {
        float temperature = subject.getTemperature();
        if (temperature >= 30) {
            System.out.println("LEDDisplay - Temperature high: Red signal");
        } else if (temperature <= 10) {
            System.out.println("LEDDisplay - Temperature low: Blue signal");
        } else {
            System.out.println("LEDDisplay - Temperature normal: Green signal");
        }
	}
}
