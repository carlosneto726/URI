import java.io.IOException;
import java.util.Scanner;
public class Media2 {

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

        double media = ((a * 2) + (b * 3) + (c * 5)) / 10;

        System.out.println(String.format("MEDIA = %.1f", media));

        input.close();
    }
 
}