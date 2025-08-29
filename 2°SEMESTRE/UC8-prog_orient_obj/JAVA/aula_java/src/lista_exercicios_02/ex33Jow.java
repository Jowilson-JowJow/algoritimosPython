//Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

package lista_exercicios_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex33Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Double> medias = new ArrayList<>();
        int aprovados = 0;
        for (int i = 1; i <= 10; i++) {
            double somaNotas = 0;
            System.out.println("\nAluno " + i + ":");
            for (int j = 1; j <= 4; j++) {
                System.out.print("Digite a " + j + "ª nota: ");
                double nota = scan.nextDouble();
                somaNotas += nota;
            }
            double media = somaNotas / 4.0;
            medias.add(media);
            if (media >= 7.0) {
                aprovados++;
            }
        }
        System.out.println("\nMédias dos alunos: " + medias);
        System.out.println("Número de alunos com média maior ou igual a 7.0: " + aprovados);
        scan.close();
    }
}
