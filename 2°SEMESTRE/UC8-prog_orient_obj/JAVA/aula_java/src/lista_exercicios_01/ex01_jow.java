//Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número digitado ao cubo.

package lista_exercicios_01;

import java.util.Scanner;

public class ex01_jow {
    public static void main (String [] args){
        Scanner scan = new Scanner (System.in);
        System.out.println("Digite um numero inteiro: ");
        int num1=scan.nextInt();
        System.out.println("Digite outro numero inteiro: ");
        int num2=scan.nextInt();
        System.out.println("Digite outro numero decimal ou inteiro: ");
        double num3=scan.nextDouble();

        System.out.printf("O 1° numero diditado foi: %d\nO 2° numero digitado foi: %d\nE o 3° numero digitado foi: %.2f",num1,num2,num3);

        double produto=num1*(num2/2);
        double soma=3*num1+num3;
        double cubo=Math.pow(num3,3);

        System.out.printf("\nO produto do 1° numero com a metade do 2° numero é %.2f\nO triplo do 1° numero somado com o 3° numero é %.2f\nO cubo do 3° numero é %.2f",produto,soma,cubo);
        scan.close();
    }
}
