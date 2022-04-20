import java.io.IOException;
import java.util.Scanner;
public class SalarioComBonus {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        
       String nome;
       double salario;
       double vendas;
       double comisao;


       nome = input.next();
       salario = input.nextDouble();
       vendas = input.nextDouble();

       comisao = (vendas * 0.15) + salario;

        System.out.println(String.format("TOTAL = R$ %.2f", comisao));
        

        
        input.close();
    }
 
}