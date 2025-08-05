//Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.

package lista_exercicios_01;

import java.util.Scanner;

public class ex24_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        while (true){
            System.out.println("--- MENU ---");
            System.out.println("1 - SOMA");
            System.out.println("2 -- SUBTRAÇÃO");
            System.out.println("3 -- MULTIPLICAÇÃO");
            System.out.println("4 -- DIVISÃO");
            System.out.println("0 -- SAIR");
            double opcao = scan.nextDouble();
            
            if(opcao == 0){
                System.out.println("Calculadora fechada!!!");
                break;
            }
            System.out.println("Digite um numero: ");
            double num1 = scan.nextDouble();
            System.out.println("Digite outro numero");
            double num2 = scan.nextDouble();
            
            double resultado = 0;
            if(opcao == 1){
                resultado=num1+num2;
                //System.out.println(num1+"+"+num2+"="+resultado);
                System.out.printf("%.2f + %.2f = %.2f ",num1,num2,resultado);
            }
            else if(opcao == 2){
                resultado=num1-num2;
                System.out.printf("%.2f - %.2f = %.2f ",num1,num2,resultado);
            }
            else if(opcao == 3){
                resultado=num1*num2;
                System.out.printf("%.2f * %.2f = %.2f ",num1,num2,resultado);
            }
            else if(opcao == 4){
                resultado=num1/num2;
                System.out.printf("%.2f / %.2f = %.2f ",num1,num2,resultado);
            }
            else{
                System.out.println("Digite uma opção valida");
            }
            
        }
        scan.close();
    }
}
