//Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.

package lista_exercicios_01;

import java.util.Scanner;

public class ex22_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite um número de 1 a 12: ");
        String num = scan.nextLine();

        if (num.equals("1")) {
            System.out.println("O mês é JANEIRO!!!");            
        }
        else if (num.equals("2")) {
            System.out.println("O mês é FEVEREIRO!!!");
        }
        else if (num.equals("3")) {
            System.out.println("O mês é MARÇO!!!");
        }
        else if (num.equals("4")) {
            System.out.println("O mês é ABRIL!!!");
        }
        else if (num.equals("5")) {
            System.out.println("O mês é MAIO!!!");
        }
        else if (num.equals("6")) {
            System.out.println("O mês é JUNHO!!!");
        }
        else if (num.equals("7")) {
            System.out.println("O mês é JULHO");
        }
        else if (num.equals("8")) {
            System.out.println("O mês é AGOSTO");
        }
        else if (num.equals("9")) {
            System.out.println("O mês é SETEMBRO");
        }
        else if (num.equals("10")) {
            System.out.println("O mês é OUTUBRO");
        }
        else if (num.equals("11")) {
            System.out.println("O mês é NOVEMBRO");
        }
        else if (num.equals("12")) {
            System.out.println("O mês é DEZEMBRO");
        }
        else {
            System.out.println("Número inválido!!!");
        }

        scan.close();
    }
}
