//9. Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas com os valores invertidos.

package lista_exercicios_01;

import java.util.Scanner;

public class ex09_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner ( System.in);
        System.out.println("Digite um numero: ");
        Double num=scan.nextDouble();
        System.out.println("Digite outro numero: ");
        Double num1=scan.nextDouble();
        Double num_reversi=num1;
        Double num1_reversi=num;
        System.out.printf("O primeiro numero digitado foi a= %.2f\ne o segundo numero digitado é b= %.2f\nInvertendo seus valores temos: a= %.2f e b= %.2f",num,num1,num_reversi,num1_reversi);
        scan.close();

    }
    
}
