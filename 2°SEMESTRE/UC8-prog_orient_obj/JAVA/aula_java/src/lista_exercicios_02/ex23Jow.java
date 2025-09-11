//Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
package lista_exercicios_02;

public class ex23Jow {
    public static void main(String[] args) {
        int soma = 0;
    
        for (int i = 1; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                soma += i;
            }
        }
    
        System.out.println("A soma de todos os números menores que 1000 múltiplos de 3 ou 5 é: " + soma);
    }
}
