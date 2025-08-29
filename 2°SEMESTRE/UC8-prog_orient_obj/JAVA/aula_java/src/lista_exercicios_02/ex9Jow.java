//Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

package lista_exercicios_02;

import java.util.Scanner;

public class ex9Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        int num = 0;
        int maior=0;
        int menor=1000000000;
        int i =0;
        for (i=0;i<10;i++){
            System.out.println("Digite um numero: ");
            num = scan.nextInt();
            if(num>maior){
                maior=num;
            }
            else if(num<menor){
                menor=num;
            }
            
            scan.close();
        }
        System.out.printf("O maior numero digitado foi %d\nO menor numero digitado foi %d",maior,menor);

    }
    
}
