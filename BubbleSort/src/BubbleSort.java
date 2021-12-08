
public class BubbleSort {

	public static void main(String[] args) {
		
		long time;
		int[] arrayBS = new int[9]; 
		int grenze = 8; 
		for(int i = 0; i<arrayBS.length; i++) {
		     arrayBS[i] = (int)(Math.random()*grenze); 
		}
		
		
		System.out.println("Array bevor dem Sortieren");  
        for(int i=0; i < arrayBS.length; i++){  
                System.out.print(arrayBS[i] + " ");  
        }
        
        System.out.println(); 
      
        time  = System.nanoTime();
        bubbleSort(arrayBS);
        time = System.nanoTime() - time;
       
        System.out.println("Array nach dem Sortieren" + " Zeit: " + time + " ns");  
        
        for(int i= 0; i < arrayBS.length; i++){  
                System.out.print(arrayBS[i] + " ");  
        }  
        

}  
	
	public static void bubbleSort(int[] arrayBS) {  
		
        int x = arrayBS.length;  
        int  y = 0;  
         for(int i=0; i < x; i++){  
                 for(int z=1; z < (x-i); z++){  
                          if(arrayBS[z-1] > arrayBS[z]){  
                                 y = arrayBS[z-1];  
                                 arrayBS[z-1] = arrayBS[z];  
                                 arrayBS[z] = y;  
                         }   
                 	}  
        }	
		
         
    }
		}



   
