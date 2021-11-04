
public class Rechnen {

	public static void main(String[] args) {
		
		SummeIterativ();
		fakultaetRekursiv(4);
        SummeRekursiv(6);
        HochRekursiv(3);
	}
	static int ergebnis;
	static int x = 3;
public static void SummeIterativ() {
	 
	for(int i = x-1; i > 0;i--) {
		 ergebnis = x+=i;
		   
		 
	}
	System.out.println(ergebnis);
	
}
	
	public static int fakultaetRekursiv(int x){
        if (x == 0){
            return 1;
        }
        return x * fakultaetRekursiv(x - 1);
    }
	public static int SummeRekursiv(int x) {
        if (x == 0){
            return 1;
        }
        return x + SummeRekursiv(x - 1);
	}
	public static double HochRekursiv(int x) {
    if (x == 0){
        return 1;
    }
    return Math.pow(x, HochRekursiv(x - 1));
}
}



