//Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valo251 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa termina com a mensagem “Número inválido”.

package lista_exercicios_01;

import java.util.Scanner;

public class ex18_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int num=scan.nextInt();
        if (num<0){
            System.out.println("Número Inavalido!!!");
        }
        else if(num>=0){
            int soma_num=0;
            while (num>0){
                soma_num += num%10;
                System.out.println(soma_num);
                num /=10;
                System.out.println(num);
            }
            System.out.println("a soma de seus algarismos é "+soma_num);
        }
        scan.close();
    }
}
