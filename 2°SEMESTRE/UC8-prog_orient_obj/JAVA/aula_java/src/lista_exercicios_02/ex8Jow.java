//Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
package lista_exercicios_02;

import java.util.Scanner;

public class ex8Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        // double media = 0;
        // double soma = 0;
        // for(int i=0; i<10;i++){
        //     System.out.println("Digite um número: ");
        //     double num = scan.nextDouble();
        //     if (num<0){
        //         System.out.println("Número Invalido: ");
        //     }
        //     else if(num>=0){
        //         soma= soma + num;
        //         media = soma/(i+1);
        //     }
        //     System.out.println(num);
        // }
        // System.out.println(media);
        // scan.close();
        //o codigo comentado foi a primera tentativa e que foi errado. por causa da forma que o for funciona
        int cont =0;
        double media= 0;
        double soma =0;
        while(cont<10){
            System.out.printf("Digite %d° numero: ",cont+1);
            double num = scan.nextDouble();
            if(num<0){
                System.out.println("Digite um numero positivo: ");
            }
            else if(num>=0){
                soma = soma + num;
                media= soma/(cont+1);
                cont++;
            }
            System.out.println(media);
        }
        scan.close();
    }
}
