package AulasJava_thiago;
import java.util.Scanner;

public class exemplo07_CNH {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        System.out.println("Passou no teste?");
        String teste =scan.nextLine();

        if (teste=="SIM"){
            System.out.println("ok");
        }else{
            System.out.println("que pena");
        }
        scan.close();
    }
    
}
