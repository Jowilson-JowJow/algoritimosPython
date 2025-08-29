//Crie um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex10Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Didite um numero (vou imprimir todos os numeros impares de zero até onumero escolhido): ");
        double num = scan.nextInt();
        double cont=0;
        List<Double> num_impares = new ArrayList<>();
        while(num>cont){
            if((cont+1)%2!=0){
                num_impares.add(cont+1);
            }
            cont++;
            
        }
        System.out.println(num_impares);
        scan.close();
    }
}
