// Escreva um algoritmo que leia um número inteiro entre 100 e 9999
// e imprima cada um dos algarismos que compõem o número.

package lista_exercicios_02;

import java.util.Scanner; // Importa a classe Scanner para ler entradas do teclado

public class ex18Jow {
    public static void main(String[] args) {
        // Cria um objeto Scanner para capturar a entrada do usuário
        Scanner scan = new Scanner(System.in);

        // Pede ao usuário que digite um número
        System.out.println("Digite um numero entre 100 e 9999: ");
        
        // Lê o número inteiro digitado pelo usuário
        int num_digitado = scan.nextInt();

        // Converte o número inteiro para String
        String num_text = String.valueOf(num_digitado);

        // Percorre cada caractere da String (cada algarismo do número)
        // OBS: usamos < (menor que), pois os índices vão de 0 até length() - 1
        for (int i = 0; i < num_text.length(); i++) {
            // Imprime o caractere na posição i (cada algarismo do número)
            System.out.println(num_text.charAt(i));
        }

        // Fecha o Scanner para evitar vazamento de recursos
        scan.close();
    }
}
