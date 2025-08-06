//Crie um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, Crie um programa que nos dê:
// - salário bruto.
// - quanto pagou ao INSS.
// - quanto pagou ao sindicato.
// - o salário líquido.
// calcule os descontos e o salário líquido, conforme a tabela abaixo:
// IR (11%) INSS (8%) Sindicato (5 %)
// - Salário Bruto : R$
// - Salário Líquido: R$
// Obs.: Salário Bruto - Descontos = Salário Líquido.

package lista_exercicios_01;

import java.util.Scanner;

public class ex40_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Qual o valor da hora trabalhado em R$ ");
        double valor=scan.nextDouble();
        System.out.println("Digite quantas horas foram trabalhados nesse mês:  ");
        double horas=scan.nextDouble();
        double salario_bruto=valor*horas;
        double ir = salario_bruto*0.11;
        double inss=salario_bruto*0.08;
        double sindicato=salario_bruto*0.05;
        double salario_liquido=salario_bruto-ir-inss-sindicato;
        System.out.println("Salario Bruto:____________________R$ "+salario_bruto);
        System.out.println("desconto IR:______________________R$ "+ir);
        System.out.println("Desconto INSS:____________________R$ "+inss);
        System.out.println("Desconto sindicato:_______________R$ "+sindicato+"\n");
        System.out.println("Salario Liquido:__________________R$ "+salario_liquido);
        scan.close();

    }
}
