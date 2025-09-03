// Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
// Atleta: Thiago Almeida
// Nota: 9.9
// Nota: 7.5
// Nota: 9.5
// Nota: 8.5
// Nota: 9.0
// Nota: 8.5
// Nota: 9.7
// Resultado final:
// Atleta: Thiago Almeida
// Melhor nota: 9.9
// Pior nota: 7.5
// Média: 9,04
package lista_exercicios_02;

import java.util.Scanner;

public class ex43Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite o nome do atleta: ");
        String nome = scan.nextLine();
        double[] notas = new double[7];
        double soma = 0;
        for (int i = 0; i < 7; i++) {
            System.out.print("Digite a nota " + (i + 1) + ": ");
            notas[i] = scan.nextDouble();
        }
        double melhor = notas[0];
        double pior = notas[0];

        System.out.println("\nAtleta: " + nome);
        for (int i = 0; i < 7; i++) {
            System.out.println("Nota: " + notas[i]);

            if (notas[i] > melhor) {
                melhor = notas[i];
            }
            if (notas[i] < pior) {
                pior = notas[i];
            }
        }
        for (int i = 0; i < 7; i++) {
            soma += notas[i];
        }
        soma = soma - melhor - pior;
        double media = soma / 5.0;
        System.out.println("\nResultado final:");
        System.out.println("Atleta: " + nome);
        System.out.println("Melhor nota: " + melhor);
        System.out.println("Pior nota: " + pior);
        System.out.printf("Média: %.2f\n", media);

        scan.close();
    }
}
