//Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
package lista_exercicios_02;

import java.util.Scanner;

public class ex32Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char[] vetor = new char[10];
        int qtdConsoantes = 0;
        System.out.println("Digite 10 caracteres (letras):");
        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Caractere " + (i + 1) + ": ");
            String entrada = scan.next();
            vetor[i] = entrada.charAt(0);
            if (Character.isLetter(vetor[i]) && !"aeiouAEIOU".contains(String.valueOf(vetor[i]))) {
                qtdConsoantes++;
            }
        }
        System.out.println("\nConsoantes digitadas:");
        for (char c : vetor) {
            if (Character.isLetter(c) && !"aeiouAEIOU".contains(String.valueOf(c))) {
                System.out.print(c + " ");
            }
        }
        System.out.println("\n\nQuantidade de consoantes: " + qtdConsoantes);
        scan.close();
    }
}
