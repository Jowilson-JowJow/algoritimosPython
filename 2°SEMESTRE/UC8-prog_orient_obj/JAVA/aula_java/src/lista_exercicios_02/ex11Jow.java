//Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50 primeiros números pares.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex11Jow {
        public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        double num = scan.nextDouble();
        double cont=0;
        List<Double> num_pares = new ArrayList<>();
        while(num>cont){
            if((cont)%2==0){
                num_pares.add(cont);
            }
            cont++; 
        }
        System.out.println("Os numeros pares de 0 a 100 são:\n"+num_pares);
        int soma=0;
        for (double n : num_pares){
            soma +=n;
        }
        System.out.println(soma);
        scan.close();
    }
}
