//Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou VVespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
package lista_exercicios_01;

import java.util.Scanner;

public class ex06_jow {
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        System.out.println("Qual o turno em que você estuda: \nM - Matutino\nV -Vespertino\nN - Noturno");
        String opcao=scan.nextLine();
        opcao=opcao.toLowerCase().trim();
        
        if(opcao.equals("m")){
            System.out.println("Bom Dia!");
        }
        else if(opcao.equals("v")){
            System.out.println("Boa Tarde!");
        }
        else if(opcao.equals("n")){
            System.err.println("Boa Noite!");
        }
        else{
            System.out.println("Valor Inválido!");
        }
        scan.close();
    }
}
