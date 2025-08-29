//Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.
package lista_exercicios_02;

import java.util.Scanner;
import java.util.Arrays;

public class ex30Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        int[] lista = new int[10];

        System.out.println("Digite um numero:");
        int num = scan.nextInt();
        int i =0;
        lista[0]=num;
        for(i=1;i<10;i++){
            lista[i]=lista[i-1]+num;
        }
        System.out.println("digite um valor para saber se ele esta dentro da lista criada: ");
        int num1 = scan.nextInt();
        boolean achou =Arrays.stream(lista).anyMatch(x -> x == num1);
        if(achou){
            System.out.println("A lista criada foi: "+Arrays.toString(lista));
            System.out.println("O valor procurado esta na lista!!!");
        }
        else{
            System.out.println("A lista criada foi: "+Arrays.toString(lista));
            System.out.println("O valor procurado NÃO esta na lista!!!");
        }
        scan.close();

    }
}
