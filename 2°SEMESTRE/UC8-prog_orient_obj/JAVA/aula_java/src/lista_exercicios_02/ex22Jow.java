//Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é: 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
package lista_exercicios_02;

import java.util.Scanner;
public class ex22Jow{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
    
        System.out.print("Digite um número inteiro: ");
        int numero = scan.nextInt();
    
        int soma = 0;
        boolean primeiro = true;
    
        System.out.print("Soma dos divisores de " + numero + " (excluindo ele próprio): ");
    
        for (int i = 1; i < numero; i++) {
            if (numero % i == 0) {
                soma += i;
                if (primeiro) {
                    System.out.print(i);
                    primeiro = false;
                } else {
                    System.out.print(" + " + i);
                }
            }
        }
    
            System.out.println(" = " + soma);
    
            scan.close();
    }
}
    