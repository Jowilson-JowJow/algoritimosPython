//Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex34Jow {
    public static void main( String[] args){
        Scanner scan = new Scanner(System.in);
        List<Integer> num_primos=new ArrayList<>();
        System.out.println("Digite um numero maior que 1: ");
        int num = scan.nextInt();
        int i;
        if(num<=1){
            System.out.println("Numero Errado!!!");
        }
        if (num>1){
            for(i=1; i<=num; i++){                
                if(num%i==0 ){
                    num_primos.add(i);
                }
            }
        }
        if (num_primos.size()==2){
            System.out.println("O numero digitado é primo!!!");
        }
        else{
            System.out.println("O numero digitado não é primo!!!");
        }
        scan.close();
    
    }
}


