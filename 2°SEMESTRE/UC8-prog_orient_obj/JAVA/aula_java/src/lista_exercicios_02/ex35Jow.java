//Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex35Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero inteiro:");
        int num = scan.nextInt();
        List<Integer> num_digtado = new ArrayList<>();
        for (int i=0; i<num+1; i++){
            num_digtado.add(i);
        }
        int soma = 0;
        for(int j=0; j<num_digtado.size(); j++){
            soma +=num_digtado.get(j);
        }
        System.out.println(soma);
        scan.close();
        
    }
    
}
