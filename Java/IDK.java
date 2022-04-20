import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;
public class IDK {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        int c = 0;

        while (c < 10) {
            ArrayList<String> Mn = new ArrayList<>();
            String a = input.next();
            Mn.add(a);
            c = c + 1;             
            System.out.print(Mn);        
        }

        input.close(); 
    }
}