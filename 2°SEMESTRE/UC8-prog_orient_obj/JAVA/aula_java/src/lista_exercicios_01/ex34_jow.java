//Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
//Venda mensal Comissão
//Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
//Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
//Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
//Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
//Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
//Menor que R$20.000,00 R$400,00 +14% das vendas
package lista_exercicios_01;

import java.util.Scanner;


public class ex34_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o valor da venda mensal: ");
        double vendas=scan.nextDouble();

        double comissao = 0;

        if(vendas>=100000){
            comissao=vendas*0.16+700;
            System.out.println("Suas vendas mensais foram: R$ "+vendas+"A sua comissão é de R$ "+comissao);
        }
        else if (vendas<100000 && vendas>=80000){
            comissao=vendas*0.14+650;
            System.out.println("Suas vendas mensais foram: R$ "+vendas+"A sua comissão é de R$ "+comissao);
        }
        else if (vendas<80000 && vendas>=60000){
            comissao=vendas*0.14+600;
            System.out.println("Suas vendas mensais foram: R$ "+vendas+"A sua comissão é de R$ "+comissao);
        }
        else if (vendas<60000 && vendas>=40000){
            comissao=vendas*0.14+550;
            System.out.println("Suas vendas mensais foram: R$ "+vendas+"A sua comissão é de R$ "+comissao);
        }
        else if (vendas<40000 && vendas>=20000){
            comissao=vendas*0.14+500;
            System.out.println("Suas vendas mensais foram: R$ "+vendas+"A sua comissão é de R$ "+comissao);
        }
        else if (vendas<20000){
            comissao=vendas*0.14+400;
            System.out.println("Suas vendas mensais foram: R$ "+vendas+"A sua comissão é de R$ "+comissao);
        }   
        scan.close();
    }
    
}
