//Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor do seu salário líquido.

package lista_exercicios_01;

import java.util.Scanner;

public class ex15_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite quantas horas trabalhou esse mês: ");
        Double hora=scan.nextDouble();
        Double salario = hora * 40.50;
        if (salario >2500){
            Double imposto = salario * 0.11;
            Double salario_liquido = salario - imposto;
            System.out.printf("Você trabalho %f horas nesse mês e seu salário após desconto de IR de %.2f recebera R$ %.2f",hora,imposto,salario_liquido);
        }
        else{
            System.out.printf("Você trabalho %f horas nesse mês e seu salário será de R$ %.2f",hora, salario);
            
        }
        scan.close();


    }

    
}
