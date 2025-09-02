//Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.
package lista_exercicios_02;

import java.util.Scanner;
public class ex21Jow {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double nota;
        double soma = 0;
        int contador = 0;

        System.out.println("Digite notas entre 0 e 10. Para encerrar, digite um valor fora desse intervalo.");

        while (true) {
            System.out.print("Digite uma nota: ");
            nota = scan.nextDouble();

            if (nota < 0 || nota > 10) {
                break;
            }

            soma += nota;
            contador++;
        }

        if (contador > 0) {
            double media = soma / contador;
            System.out.printf("Média das notas: %.2f\n", media);
        } else {
            System.out.println("Nenhuma nota válida foi digitada.");
        }

        scan.close();
    }
}
