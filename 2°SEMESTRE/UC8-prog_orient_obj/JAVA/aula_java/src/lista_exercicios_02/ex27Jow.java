//Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex27Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Integer> num_digitados= new ArrayList<>();
        while(true){
            System.out.println("Digite um numero: ");
            int num = scan.nextInt();
            if(num>0){
                num_digitados.add(num);
            }
            else{
                System.out.println("O codigo sera encerrado!!!");
                break;
            }
        }
        System.out.println(num_digitados);
        int maior = num_digitados.get(0);
        int menor = num_digitados.get(0);
        for(int i=1; i<num_digitados.size();i++){
            if(num_digitados.get(i)>maior){
                maior = num_digitados.get(i);
            }
            else if(num_digitados.get(i)<menor){
                menor = num_digitados.get(i);
            }
        }
        System.out.println(maior);
        System.out.println(menor);
        scan.close();

    }
}
