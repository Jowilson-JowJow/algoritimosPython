//Crie um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex13_jow {
           public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        double num = scan.nextDouble();
        double cont=0;
        List<Double> num_pares = new ArrayList<>();
        while(num+1>cont){
            if((cont)%2==0){
                num_pares.add(cont);
            }
            cont++; 
        }
        System.out.println("Os numeros pares de 0 a 100 são:\n"+num_pares);

        scan.close();
    }
}
