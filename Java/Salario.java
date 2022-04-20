import java.io.IOException;
import java.util.Scanner;
public class Salario {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        
        int num = input.nextInt();
        double hour = input.nextDouble();
        double salhour = input.nextDouble();

        double sal = (hour * salhour);

        System.out.println(String.format("NUMBER = " + num));
        System.out.println(String.format("SALARY = U$ %.2f", sal));
        input.close();
    }
 
}