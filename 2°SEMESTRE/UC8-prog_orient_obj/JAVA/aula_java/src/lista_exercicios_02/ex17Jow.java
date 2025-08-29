//Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A quantidade de números a serem lidos deve será fornecida pelo usuário.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex17Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Quantos Numeros será digitado: ");
        int num = scan.nextInt();
        int cont = 0;
        List<Integer> lista = new ArrayList<>();
     //erro nessa linha "Int cannot be resolved to a type"
        while(cont<num){
            System.out.println("Digite um numero: ");
            int num1 = scan.nextInt();
            lista.add(num1);
            cont++;
        }
        System.out.println(lista);
        int maior = lista.get(0);
        for(int i =1; i<lista.size();i++){
            if(lista.get(i)>maior){
                maior = lista.get(i);
            }
        }
        System.out.println("O maior número é: "+maior);
        scan.close();
    }

}

