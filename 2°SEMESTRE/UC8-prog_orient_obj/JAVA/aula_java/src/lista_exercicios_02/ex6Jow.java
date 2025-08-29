//Escreva um programa que peça ao usuário para digitar 10 valores e some-os.
package lista_exercicios_02;

import java.util.Scanner;

public class ex6Jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        int i=0;
        int x = 0;
        for(i=0;i<10;i++){
            System.out.printf("digite o %d° numero: ",i+1);
            int num = scan.nextInt();
            x = x +num;
        }
        System.out.println("A soma dos numeros digitados é: "+x);
        scan.close();
    }
    
}
