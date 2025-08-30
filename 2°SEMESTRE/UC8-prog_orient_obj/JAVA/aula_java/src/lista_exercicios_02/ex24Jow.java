package lista_exercicios_02;
import java.util.Scanner;

public class ex24Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int idade;
        int soma = 0;
        int contador = 0;

        System.out.println("Digite as idades (0 para encerrar):");

        while (true) {
            System.out.print("Idade: ");
            idade = scan.nextInt();

            if (idade == 0) {
                break;
            }

            soma += idade;
            contador++;
        }

        if (contador > 0) {
            double media = (double) soma / contador;
            System.out.printf("A idade média do grupo é: %.2f\n", media);
        } else {
            System.out.println("Nenhuma idade válida foi digitada.");
        }

        scan.close();
    }
}
