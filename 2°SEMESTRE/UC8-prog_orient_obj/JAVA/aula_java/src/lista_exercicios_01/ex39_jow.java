//Crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
//- comprar apenas latas de 18 litros;
//- comprar apenas galões de 3,6 litros;
package lista_exercicios_01;

import java.util.Scanner;

public class ex39_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite o tamanho da área a ser pintada (em m²): ");
        double area = scan.nextDouble();
        double litros = area / 6;
        litros *= 1.1;
        int latas18L = (int) Math.ceil(litros / 18.0);//Math.ceil() garante que mesmo 1 litro a mais exige uma nova lata inteira.
        double precoLatas = latas18L * 80.0;
        int galoes36L = (int) Math.ceil(litros / 3.6);//Math.ceil() garante que mesmo 1 litro a mais exige uma nova lata inteira.
        double precoGaloes = galoes36L * 25.0;
        System.out.println("\n== OPÇÕES DE COMPRA ==");
        System.out.println("1) Apenas latas de 18L:");
        System.out.println("   Quantidade: " + latas18L + " lata(s)");
        System.out.printf("   Preço total: R$ %.2f\n", precoLatas);
        System.out.println("\n2) Apenas galões de 3,6L:");
        System.out.println("   Quantidade: " + galoes36L + " galão(ões)");
        System.out.printf("   Preço total: R$ %.2f\n", precoGaloes);

        scan.close();
    }
}

