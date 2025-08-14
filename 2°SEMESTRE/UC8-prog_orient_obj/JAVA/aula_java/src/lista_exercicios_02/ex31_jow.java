//Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores.
package lista_exercicios_02;

import java.util.Arrays;
import java.util.Scanner;

public class ex31_jow {
        public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        int[] lista = new int[20];
        int i =0;
        for(i=1;i<20;i++){
            System.out.printf("Digite o %d° numero: ",i);
            int num = scan.nextInt();
            lista[i]=num;
        }
        System.out.println(Arrays.toString(lista));
        // int num1 = scan.nextInt();
        // boolean achou =Arrays.stream(lista).anyMatch(x -> x == num1);
        // if(achou){
        //     System.out.println("A lista criada foi: "+Arrays.toString(lista));
        //     System.out.println("O valor procurado esta na lista!!!");
        // }
        // else{
        //     System.out.println("A lista criada foi: "+Arrays.toString(lista));
        //     System.out.println("O valor procurado NÃO esta na lista!!!");
        // }
        // scan.close();

    }
}
