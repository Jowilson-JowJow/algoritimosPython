//Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
package lista_exercicios_02;

import java.util.Scanner;

public class ex38Jow{
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        double num;
        double quadrado;
        double cubo;
        double raiz;
        while (true){
            System.out.println("Digite um numero: ");
            num=scan.nextDouble();
            quadrado=Math.pow(num,2);
            cubo=Math.pow(num,3);
            raiz=Math.sqrt(num);
            System.out.printf("O numero digitado é %.0f\no seu quadrado é %.2f\no seu cubo é: %.2f\na sua raiz quadrada é: %.2f\n",num,quadrado,cubo,raiz);
            if(num<=0){
                System.out.println("ERROR!!!");
                break;
            }
        }
        scan.close();

    }

}

