import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        
        String if1 = input.next();
        String if2 = input.next();

        String[] info1 = if1.split(" "); 
        String[] info2 = if2.split(" "); 

        int info1qtd = Integer.parseInt(info1[1]);
        int info1val = Integer.parseInt(info1[2]);

        int info2qtd = Integer.parseInt(info2[1]);
        int info2val = Integer.parseInt(info2[2]);

        int total = (info1qtd * info1val) + (info2qtd * info2val);
            
        System.out.println(total);

    

        input.close();
    }
 
}