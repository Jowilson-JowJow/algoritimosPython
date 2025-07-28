package AulasJava_thiago;
//declarar o scanner -->> input para isso deve-se importar o java.util.Scanner
import java.util.Scanner;

public class exemplo09 {
    public static void main(String[] args){
        //declarar o scaner dentro da main
        Scanner scan = new Scanner (System.in);
        System.out.println("Digite a sua idade: ");
        int num = scan.nextInt();
        if(num>=18){
            System.out.println("Maior !!!");
        }
        else{
            System.out.println("menor !!!");
        }

        scan.close();//sempre que abrir o scan deve fechar o scan
    }
}
