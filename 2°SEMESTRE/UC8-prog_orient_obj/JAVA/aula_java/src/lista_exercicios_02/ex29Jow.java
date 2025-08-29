//Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.
package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex29Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int i = 0;
        List<Integer> lista = new ArrayList<>();
        int soma=0;
        for(i=0;i<5;i++){
            System.out.println("digite um numero: ");
            int num = scan.nextInt();
            lista.add(num);
            soma+=num;
        }
        for(i=0;i<5;i++){
            System.out.printf("O %d° numero digitado foi: %d\n",i,lista.get(i)); 
        }
        System.out.println("A soma dos numeros digitados é: "+soma);
        scan.close();

    }
    
}
