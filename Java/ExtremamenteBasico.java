import java.util.Scanner;
import java.io.IOException;
public class ExtremamenteBasico {

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        
        int A = input.nextInt();
        int B = input.nextInt();
        int X = A + B;

        System.out.println("X = "+ X);

        input.close();
    }

}