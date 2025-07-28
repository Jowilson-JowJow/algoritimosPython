package AulasJava_thiago;
import java.util.Scanner;

public class exemplo10 {
    public static void main(String[] args) {
        int idade;
        Scanner input=new Scanner(System.in);
        System.out.println("Digite a sua idade: ");
        idade=input.nextInt();

        if(idade <=12){
            System.out.println("Criança!!");
        }
        else if(idade>12 && idade<=17){
            System.out.println("Adolescente!!");
        }
        else if(idade>17 && idade<=59){
            System.out.println("Adulto!!!");
        }
        else{
            System.out.println("Idoso!!");
        }
        input.close();
    }
}
