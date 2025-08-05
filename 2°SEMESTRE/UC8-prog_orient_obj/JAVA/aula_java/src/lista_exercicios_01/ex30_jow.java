//Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
//Consumo (Km/l) Mensagem
//menor que 8 Venda o carro!
//entre 8 e 14 Econômico!
//maior que 14 Super econômico!

package lista_exercicios_01;
import java.util.Scanner;
public class ex30_jow {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite a distância percorrida (em Km): ");
        double distancia = entrada.nextDouble();

        System.out.print("Digite a quantidade de litros de gasolina consumidos: ");
        double litros = entrada.nextDouble();

        double consumo = distancia / litros;

        System.out.printf("\nConsumo: %.2f Km/l\n\n", consumo);

        System.out.println("+-------------------+-------------+---------------------+");
        System.out.println("| Faixa de Consumo  |   (Km/l)    | Mensagem            |");
        System.out.println("+-------------------+-------------+---------------------+");

        if (consumo < 8) {
            System.out.println("| menor que         |     8       | Venda o carro!      |");
        } else if (consumo >= 8 && consumo <= 14) {
            System.out.println("| entre             |  8 e 14     | Econômico!          |");
        } else {
            System.out.println("| maior que         |    14       | Super econômico!    |");
        }

        System.out.println("+-------------------+-------------+---------------------+");

        entrada.close();
    }
}

