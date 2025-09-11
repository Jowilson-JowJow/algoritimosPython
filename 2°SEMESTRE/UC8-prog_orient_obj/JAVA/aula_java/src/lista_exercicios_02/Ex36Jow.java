//Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de tela de saída:
// Digite o valor inicial e valor final: 5
// 10
// Soma dos ímpares neste intervalo: 21


package lista_exercicios_02;
import java.util.ArrayList;
import java.util.List; 
import java.util.Scanner;
public class Ex36Jow {    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um valor de inicio e um valor de final:");
        int inicio = scan.nextInt();
        int fim = scan.nextInt();
        List<Integer> lista_impar = new ArrayList<>();
        for (int i = inicio; i <= fim; i++) {
            if (i % 2 != 0) {
                lista_impar.add(i);
            }
        }
        System.out.println("Os numeros impares no intervalo dos numeros digitados são: " + lista_impar);
        int soma = 0;
        for (int j = 0; j < lista_impar.size(); j++) {
            soma += lista_impar.get(j);
        }
        System.out.println("A soma dos numeros impares é: " + soma);
        scan.close();
    }
}

