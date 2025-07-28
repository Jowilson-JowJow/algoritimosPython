package AulasJava_thiago;
import java.util.Scanner;

public class exemplo11 {
    public static void main(String[] args) {
        
        Scanner scan=new Scanner(System.in);
        System.out.println("Digite SIM/NÂO");
        String confirmacao=scan.next();
        System.out.println("Texto digitado: "+confirmacao);
        scan.close();
    }
}
