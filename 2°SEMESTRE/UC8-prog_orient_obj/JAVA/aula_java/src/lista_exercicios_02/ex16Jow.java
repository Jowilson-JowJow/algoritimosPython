//Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.
package lista_exercicios_02;

import java.util.Scanner;

public class ex16Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero (vamos somar todos os numeros até o valor digitado): ");
        int num = scan.nextInt();
        int soma = 0;
        for (int i=0;i<num;i++){
            soma = soma+(i+1);
        }
        System.out.printf("A soma dos numeros naturais entre 0 e %d é: %d",num,soma);
        scan.close();
    }
}
