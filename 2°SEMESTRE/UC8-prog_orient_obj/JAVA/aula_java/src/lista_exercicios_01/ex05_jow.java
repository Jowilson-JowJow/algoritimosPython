//5. Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F - Feminino, M – Masculino ou Sexo Inválido.
package lista_exercicios_01;

import java.util.Scanner;

public class ex05_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite\nF - para feminino\nM - para masculino");
        String word = scan.nextLine();
        word=word.toLowerCase().trim();// letras devem ser digitadas tanto em maiúsculas quanto minúsculas (F, f, M, m) e serão tratadas corretamente! Se quiser deixar ainda mais robusto, pode também fazer um .trim() para remover espaços antes/depois:

        if (word.equals("f")){
            System.out.println("Feminino");
        }
        else if (word.equals("m")){
            System.out.println("Masculino");
        }
        else{
            System.out.println("sexo invalido");
        }
        scan.close();
    }

}
