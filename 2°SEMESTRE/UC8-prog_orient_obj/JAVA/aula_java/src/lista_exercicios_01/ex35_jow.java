// //Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que
// considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
// salário terão um aumento proporcionalmente maior do que os funcionários com um salário
// maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
// adicional de salário. Crie um programa que leia:
// • o valor do salário atual do funcionário;
// • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na
// empresa).
// Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do
// salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum
// aumento.
// Salário Atual Reajuste (%) Tempo de Serviço Bônus
// Até 500,00 25% Abaixo de 1 ano Sem bônus
// Até 1000,00 20% De 1 a 3 anos 100,00
// 5
// Até 1500,00 15% De 4 a 6 anos 200,00
// Até 2000,00 10% De 7 a 10 anos 300,00
// Acima de 2000,00 Sem reajuste Mais de 10 anos 500,00
package lista_exercicios_01;

import java.util.Scanner;

public class ex35_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o salario atual: ");
        double salario = scan.nextDouble();
        System.out.println("Digite o tempo de empresa (em meses): ");
        double tempo = scan.nextDouble();

        double novo_salario=0;
        if(salario<=500 && tempo<12){
            novo_salario=salario*1.25;
            System.out.println("seu novo salario é de R$ "+novo_salario);
        }
        else if(salario<=1000 && tempo<=36){
            novo_salario=salario*1.20+100;
            System.out.println("seu novo salario é de R$ "+novo_salario);
        }
        else if(salario<=1500 && tempo<=72){
            novo_salario=salario*1.15+200;
            System.out.println("seu novo salario é de R$ "+novo_salario);
        }
        else if(salario<=2000 && tempo<=120){
            novo_salario=salario*1.10+300;
            System.out.println("seu novo salario é de R$ "+novo_salario);
        }
        else if(salario>=2000 && tempo>=120){
            novo_salario=salario+500;
            System.out.println("seu novo salario é de R$ "+novo_salario);
        }
        scan.close();

    }
    
}
