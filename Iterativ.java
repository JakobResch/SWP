
public class Iterativ {

	public static void main(String[] args) {
		
		SummeIterativ();
		
	}
	static int ergebnis;
	static int x = 3;
public static void SummeIterativ() {
	 
	for(int i = x-1; i > 0;i--) {
		 ergebnis = x+=i;
		   
		 
	}
	System.out.println(ergebnis);
	
}

}
