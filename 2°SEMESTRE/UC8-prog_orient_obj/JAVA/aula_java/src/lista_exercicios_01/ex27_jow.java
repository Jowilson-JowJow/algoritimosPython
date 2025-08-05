//Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os dois números recebidos. Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
//1- Soma de 2 números.
//2- Diferença entre 2 números (maior pelo menor).
//3- Produto entre 2 números.
//4- Divisão entre 2 números (o denominador não pode ser zero).
package lista_exercicios_01;

import java.util.Scanner;

public class ex27_jow {
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
                if(num1>num2){
                    resultado=num1-num2;
                    System.out.printf("%.2f - %.2f = %.2f ",num1,num2,resultado);                
                }
                else{
                    resultado=num2-num1;
                    System.out.printf("%.2f - %.2f = %.2f ",num2,num1,resultado); 
                }
            }
            else if(opcao == 3){
                resultado=num1*num2;
                System.out.printf("%.2f * %.2f = %.2f ",num1,num2,resultado);
            }
            else if(opcao == 4){
                if(num2==0){
                    System.out.println("O denominador é zero!!!\nA divisão da erro!!!");
                }
                else{
                    resultado=num1/num2;
                    System.out.printf("%.2f / %.2f = %.2f ",num1,num2,resultado);
                }
            }
            else{
                System.out.println("Digite uma opção valida");
            }
            
        }
        scan.close();
    }
}
