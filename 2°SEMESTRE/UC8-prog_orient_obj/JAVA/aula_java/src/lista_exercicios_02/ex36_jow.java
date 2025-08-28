//Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de tela de saída:
// Digite o valor inicial e valor final: 5
// 10
// Soma dos ímpares neste intervalo: 21
package lista_exercicios_02;

import java.util.Scanner;

public class ex36_jow {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        System.out.println("Digite um valor de inicio e um valor de final:");
        int inicio=scan.nextInt();
        int final=scan.nextInt();

    }
    
}
