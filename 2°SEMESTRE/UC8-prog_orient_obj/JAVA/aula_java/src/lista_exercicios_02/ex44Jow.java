// Crie um programa para a Academia BemMaisFort. Neste programa você deve receber os dados de 25 pessoas. Sendo: Idade, Sexo, Altura, Peso. No final o programa deve calcular e imprimir:
// • a idade da pessoa mais velha;
// • a altura do mais alto;
// • o maior peso;
// • a média de Altura e a Média de IMC;
// • porcentagem de Sexo Masculino;
// • porcentagem de Sexo Feminino;
package lista_exercicios_02;

import java.util.Scanner;

public class ex44Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        final int TOTAL_PESSOAS = 25;
        int idadeMaisVelha = 0;
        double alturaMaisAlta = 0;
        double maiorPeso = 0;
        double somaAltura = 0;
        double somaIMC = 0;
        int contadorMasculino = 0;
        int contadorFeminino = 0;
        for (int i = 1; i <= TOTAL_PESSOAS; i++) {
            System.out.println("\nPessoa " + i);
            System.out.print("Digite a idade: ");
            int idade = scan.nextInt();
            System.out.print("Digite o sexo (M/F): ");
            char sexo = scan.next().toUpperCase().charAt(0);
            System.out.print("Digite a altura (em metros): ");
            double altura = scan.nextDouble();
            System.out.print("Digite o peso (em kg): ");
            double peso = scan.nextDouble();
            if (idade > idadeMaisVelha) {
                idadeMaisVelha = idade;
            }
            if (altura > alturaMaisAlta) {
                alturaMaisAlta = altura;
            }
            if (peso > maiorPeso) {
                maiorPeso = peso;
            }
            somaAltura += altura;
            double imc = peso / (altura * altura);
            somaIMC += imc;
            if (sexo == 'M') {
                contadorMasculino++;
            } else if (sexo == 'F') {
                contadorFeminino++;
            } else {
                System.out.println("Sexo inválido. Não será contabilizado.");
            }
        }
        double mediaAltura = somaAltura / TOTAL_PESSOAS;
        double mediaIMC = somaIMC / TOTAL_PESSOAS;
        double percMasculino = (contadorMasculino * 100.0) / TOTAL_PESSOAS;
        double percFeminino = (contadorFeminino * 100.0) / TOTAL_PESSOAS;
        System.out.println("\n===== RESULTADOS =====");
        System.out.println("Idade da pessoa mais velha: " + idadeMaisVelha + " anos");
        System.out.printf("Altura da pessoa mais alta: %.2f m\n", alturaMaisAlta);
        System.out.printf("Maior peso: %.2f kg\n", maiorPeso);
        System.out.printf("Média de altura: %.2f m\n", mediaAltura);
        System.out.printf("Média de IMC: %.2f\n", mediaIMC);
        System.out.printf("Porcentagem de homens: %.2f%%\n", percMasculino);
        System.out.printf("Porcentagem de mulheres: %.2f%%\n", percFeminino);
        scan.close();
    }
}
