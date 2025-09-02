//Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência igual a zero.
package lista_exercicios_02;

import java.util.Scanner;

public class ex37Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int r1, r2;
        double req;
        while (true) {
            System.out.println("Digite o valor para o R1: ");
            r1 = scan.nextInt();
            System.out.println("Digite o valor para o R2: ");
            r2 = scan.nextInt();
            if (r1 == 0 || r2 == 0) {
                System.out.println("Programa encerrado.");
                break;
            }
            req = (r1 * r2) / (double)(r1 + r2);
            System.out.println("A resistência equivalente entre os resistores R1 e R2 em paralelo é: " + req);
        }
        scan.close();
    }
}
