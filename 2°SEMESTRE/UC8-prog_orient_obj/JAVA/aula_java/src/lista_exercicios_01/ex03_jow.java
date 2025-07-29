
//Crie um programa que receba dois números e mostre qual deles é o maior.
package lista_exercicios_01;

import java.util.Scanner;

public class ex03_jow {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int num1=scan.nextInt();
        System.out.println("Digite outro umero: ");
        int num2=scan.nextInt();
        if (num1>num2){
            System.out.printf("O numero %d é Maior que %d",num1,num2);
        }
        else{
            System.out.printf("O numero %d é MAIOR que %d",num2,num1);
        }
        scan.close();
    }
    
}
