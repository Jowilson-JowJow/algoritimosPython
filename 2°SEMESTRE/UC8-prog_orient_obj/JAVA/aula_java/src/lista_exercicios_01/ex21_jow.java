//Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.

package lista_exercicios_01;

import java.util.Scanner;

public class ex21_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite um número de 1 a 7: ");
        String num = scan.nextLine();

        if (num.equals("1")) {
            System.out.println("Hoje é DOMINGO!!!");            
        } else if (num.equals("2")) {
            System.out.println("Hoje é SEGUNDA-FEIRA!!!");
        } else if (num.equals("3")) {
            System.out.println("Hoje é TERÇA-FEIRA!!!");
        } else if (num.equals("4")) {
            System.out.println("Hoje é QUARTA-FEIRA!!!");
        } else if (num.equals("5")) {
            System.out.println("Hoje é QUINTA-FEIRA!!!");
        } else if (num.equals("6")) {
            System.out.println("Hoje é SEXTA-FEIRA!!!");
        } else if (num.equals("7")) {
            System.out.println("Hoje é SÁBADO!!!");
        } else {
            System.out.println("Número inválido!!!");
        }

        scan.close();
    }
}
