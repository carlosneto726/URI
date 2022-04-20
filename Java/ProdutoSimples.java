import java.io.IOException;
import java.util.Scanner;
public class ProdutoSimples {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int prod = a * b;
        System.out.println("PROD = " + prod);
        input.close();
 
    }
 
}