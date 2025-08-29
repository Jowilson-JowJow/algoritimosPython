//Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem crescente.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex15Jow {
               public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        double num = scan.nextDouble();
        double cont=0;
        List<Double> num_impares = new ArrayList<>();
        while(num+1>cont){
            if((cont)%2!=0){
                num_impares.add(cont);
            }
            cont++; 
        }

        System.out.println("Os numeros pares de 0 a 100 em ordem decrescente são:\n"+num_impares);

        scan.close();
    }
}
