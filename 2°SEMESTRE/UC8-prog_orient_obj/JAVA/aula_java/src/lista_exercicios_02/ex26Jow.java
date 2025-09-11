//Escreva um programa que calcule e escreva o valor de S=1/1+3/2+5/3+7/4+...99/50

package lista_exercicios_02;

public class ex26Jow {

    public static void main(String[] args) {
        double soma = 0.0;

        for (int n = 1; n <= 50; n++) {
            double termo = (2.0 * n - 1) / n;
            soma += termo;
            System.out.println(soma);
        }

        System.out.printf("A soma da sequência é: %.3f\n", soma);
    }
}

