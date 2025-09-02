//Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020 recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa que determine o salário atual do funcionário.
package lista_exercicios_02;

import java.util.Scanner;

public class ex28Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite o ano atual (ex: 2025): ");
        int ano_atual = scan.nextInt();
        int ano_contratado = 2019;
        int anos = ano_atual - ano_contratado;

        if (anos == 0) {
            System.out.println("Tem menos de um ano de contratação, sem aumento.");
        } else {
            double salario = 4000.0;
            double taxaAumento = 0.015;

            for (int i = 1; i <= anos; i++) {
                salario = salario + salario * taxaAumento;
                if (i >= 2) {
                    taxaAumento = taxaAumento * 2;
                }
            }

            System.out.printf("Salário atual em %d é: R$ %.2f\n", ano_atual, salario);
        }

        scan.close();
    }
}
