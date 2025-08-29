//Escreva um programa que leia 10 inteiros e imprima sua média.
package lista_exercicios_02;

import java.util.Scanner;

public class ex7Jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        int i=0;
        int x = 0;
        for(i=0;i<10;i++){
            System.out.printf("digite o %d° numero: ",i+1);
            int num = scan.nextInt();
            x = x +num;
        }
        double media = x/10.0;
        System.out.printf("A média dos numeros digitados é: %.2f",media);
        scan.close();
    }
    
}