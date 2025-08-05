//Determine se um determinado ano lido é bissexto. Sendo que um ano e bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.

package lista_exercicios_01;

import java.util.Scanner;

public class ex25_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um ano para verificar se ele é bisexto: ");
        int ano = scan.nextInt();
        if(ano%400==0 && ano%4==0){
            System.out.println("O ano ínformado é um ano bisexto!!!");
        }
        else{
            System.out.println("O ano informado Não é um ano bisexto!!!");
        }
        scan.close();
    }
    
}
