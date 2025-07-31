// Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
package lista_exercicios_01;

import java.util.Scanner;

public class ex08_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner ( System.in);
        System.out.println("Digite um numero para extrair a sua raiz quadrada: ");
        Double num=scan.nextDouble();
        Double raiz_num=Math.sqrt(num);
        System.out.printf("A raiz quadrado de %.2f é %.2f%n", num,raiz_num);
        scan.close();
    }
    
}
