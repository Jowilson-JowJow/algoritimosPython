//Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos e número de valores pares. O processo termina quando for digitado o número 0.
package lista_exercicios_02;

import java.util.Scanner;
public class ex19Jow {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int numero;
        int qtdLidos = 0;
        int qtdPares = 0;

        do {
            System.out.print("Digite um número inteiro (0 para encerrar): ");
            numero = scan.nextInt();

            if (numero != 0) {
                qtdLidos++;

                if (numero % 2 == 0) {
                    System.out.println(numero + " é PAR");
                    qtdPares++;
                } else {
                    System.out.println(numero + " é ÍMPAR");
                }
            }
        } while (numero != 0);

        System.out.println("\nResumo:");
        System.out.println("Quantidade de números lidos: " + qtdLidos);
        System.out.println("Quantidade de números pares: " + qtdPares);

        scan.close();
    }
}
