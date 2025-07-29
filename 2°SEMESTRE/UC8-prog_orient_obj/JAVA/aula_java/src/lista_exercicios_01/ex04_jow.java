//4. Crie um programa que receba três números e mostre-os se estão em ordem crescente.

package lista_exercicios_01;

import java.util.Scanner;

public class ex04_jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o primeiro numero: ");
        int num1 = scan.nextInt();
        System.out.println("Digite o segundo numero: ");
        int num2 = scan.nextInt();
        System.out.println("Digite o terceiro numero: ");
        int num3 = scan.nextInt();
        if (num1<num2 && num2<num3 ){
            System.out.printf("Os numeros digitados foram %d , %d e %d\n  e estão em ordem crescente.",num1,num2,num3);
        }
        else{
            System.out.printf("Os numeros digitados foram %d , %d e %d\n  e NÃO estão em ordem crescente.",num1,num2,num3);
        }
        scan.close();
    }
}
