import java.io.IOException;
import java.util.Scanner;
public class ConversaoDeTempo {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        
        double n = input.nextDouble();

        double h = ((n / 60) / 60);
        int horas = (int) h;

        double m = (h - horas) * 60;
        int minutos = (int) m;
        
        double s = (m - minutos) * 60;
        
        System.out.println(String.format("%d:%d:%.0f", horas, minutos, s));
        input.close();
    }
 
}