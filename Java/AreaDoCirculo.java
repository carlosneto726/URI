import java.util.Scanner;
import java.io.IOException;
public class AreaDoCirculo {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);

        double raio = input.nextDouble();
        double area = 3.14159 * Math.pow(raio, 2);

        System.out.println(String.format("A=%.4f", area));
        input.close();
    }
 
}