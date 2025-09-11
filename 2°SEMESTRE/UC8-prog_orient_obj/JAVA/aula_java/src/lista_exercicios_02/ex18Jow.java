// Escreva um algoritmo que leia um número inteiro entre 100 e 9999
// e imprima cada um dos algarismos que compõem o número.

package lista_exercicios_02;

import java.util.Scanner;

public class ex18Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero entre 100 e 9999: ");
        int num_digitado = scan.nextInt();
        String num_text = String.valueOf(num_digitado);
        for (int i = 0; i < num_text.length(); i++) {         
            System.out.println(num_text.charAt(i));
        }

        scan.close();
    }
}
