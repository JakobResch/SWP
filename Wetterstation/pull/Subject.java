package pull;

public interface Subject {
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    float getTemperature();
    float getHumidity();
}