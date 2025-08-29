//Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class ex31Jow {
        public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        int[] lista = new int[20];
        List<Integer> lista_par = new ArrayList<>();
        List<Integer> lista_impar = new ArrayList<>();
        int i =0;
        for(i=0;i<20;i++){
            System.out.printf("Digite o %d° numero: ",i+1);
            int num = scan.nextInt();
            lista[i]=num;
            if (num%2==0){
                lista_par.add(num);
            }
            else{
                lista_impar.add(num);
            }
            scan.close();
        }
        System.out.println(Arrays.toString(lista));
        System.out.println(lista_par);
        System.out.println(lista_impar);

    }
}
