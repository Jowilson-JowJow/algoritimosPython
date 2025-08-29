//Crie um programa que receba dois números. Calcule e mostre:
//• a soma dos números pares desse intervalo de números, incluindo os números digitados;
//• a multiplicação dos números ímpares desse intervalo, incluindo os digitados;
package lista_exercicios_02;

import java.util.Scanner;

public class ex20Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        int num1 = scan.nextInt();

        int inicio = Math.min(num, num1);
        int fim = Math.max(num, num1);

        int somaPares = 0;
        int multImpares = 1;
        boolean temImpar = false;

        for (int i = inicio; i <= fim; i++) {
            if (i % 2 == 0) {
                somaPares += i;
            } else {
                multImpares *= i;
                temImpar = true;
            }
        }

        if (!temImpar) {
            multImpares = 0;
        }

        System.out.println("Soma dos números pares: " + somaPares);
        System.out.println("Multiplicação dos números ímpares: " + multImpares);

        scan.close();
    }
}
