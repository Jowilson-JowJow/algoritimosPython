//Crie um programa que receba um número inteiro e verifique se ele é maior que 10 se sim, imprima: é maior que 10, senão imprima: é menor que 10.

package lista_exercicios_01;


import java.util.Scanner;

public class ex02_jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero : ");
        int num=scan.nextInt();

        if (num>=10){
            System.out.println("O numero digitdo é MAIOR que 10.");
        }
        else{
            System.out.println("O numero digitado é MENOR que 10.");
        }
        scan.close();

    }

    
}
