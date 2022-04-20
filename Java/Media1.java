import java.util.Scanner;
import java.io.IOException;
public class Media1 {

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble();
        double b = input.nextDouble();
        double media = ((a * 3.5) + (b * 7.5)) / (3.5 + 7.5);

        System.out.println(String.format("MEDIA = %.5f", media));

        input.close();

    }

}