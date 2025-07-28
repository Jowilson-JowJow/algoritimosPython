package AulasJava_thiago;
//declarar o scanner -->> input para isso deve-se importar o java.util.Scanner
import java.util.Scanner;

public class exemplo08 {
    public static void main(String[] args){
        //declarar o scaner dentro da main
        Scanner scan = new Scanner (System.in);
        System.out.println("Digite um numero: ");
        int num = scan.nextInt();
        System.out.println(num);
        scan.close();//sempre que abrir o scan deve fechar o scan
    }
}
