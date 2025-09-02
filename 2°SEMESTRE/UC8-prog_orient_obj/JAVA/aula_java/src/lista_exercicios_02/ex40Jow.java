//Crie um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números.
// • adição (opção 1)
// • subtração (opção 2) • multiplicação (opção 3)
// • divisão (opção 4).
// • saída (opção 5)
// • programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).
package lista_exercicios_02;

import java.util.Scanner;

public class ex40Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        while (true){
            System.out.println("Digite dois numeros, e depois escolha qual operação deseja fazer.");
            double num1 = scan.nextDouble();
            double num2 = scan.nextDouble();
            System.out.println("****CALCULADORA****");
            System.out.println("1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - SAÍDA");
            int escolha=scan.nextInt();
            double resultado=0;
            if(escolha==1){
                resultado=num1+num2;
                System.out.printf("%.2f + %.2f = %.2f",num1,num2,resultado);
            }
            else if(escolha==2){
                resultado=num1-num2;
                System.out.printf("%.2f - %.2f = %.2f",num1,num2,resultado);
            }
            else if(escolha==3){
                resultado=num1*num2;
                System.out.printf("%.2f x %.2f = %.2f",num1,num2,resultado);
            }
            else if(escolha==4){
                resultado=num1/num2;
                System.out.printf("%.2f / %.2f = %.2f",num1,num2,resultado);
            }
            else if(escolha==5){
                System.out.println("Saindo da Calculadora!!!");
                break;
            }
        }
        scan.close();
    }
}
