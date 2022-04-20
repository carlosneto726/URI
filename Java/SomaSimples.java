import java.io.IOException;
import java.util.Scanner;

public class SomaSimples {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int soma = a + b;
        System.out.println("SOMA = " + soma);
        input.close();
      
    }
 
}
