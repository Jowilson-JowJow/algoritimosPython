//Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
//• O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
//• Chama-se equilátero o triângulo que tem três lados iguais.
//• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
//• Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
package lista_exercicios_01;

import java.util.Scanner;

public class ex26_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o 1° lado do triangulo: ");
        int lado_a=scan.nextInt();
        System.out.println("Digite o 2° lado do triangulo: ");
        int lado_b=scan.nextInt();
        System.out.println("Digite o 3° lado do triangulo: ");
        int lado_c=scan.nextInt();
        if(lado_a==lado_b && lado_a==lado_c){
            System.out.printf("O lado a = %d\nO lado b = %d\nO lado c = %d\nportanto o tringulo é EQUILATERO!!!",lado_a,lado_b,lado_c);
        }
        else if(lado_a==lado_b && lado_a!=lado_c){
            System.out.printf("O lado a = b = %d\nO lado c = %d\nO triangulo é ISÓCELES!!!",lado_a,lado_c);
        }
        else if(lado_a==lado_c && lado_a!=lado_b){
            System.out.printf("O lado a = c = %d\nO lado b = %d\nO triangulo é ISÓCELES!!!",lado_a,lado_b);
        }
        else if(lado_b==lado_c && lado_b!=lado_a){
            System.out.printf("O lado b = c = %d\nO lado a = %d\nO triangulo é ISÓCELES!!!",lado_b,lado_a);
        }
        else if(lado_a!=lado_b && lado_a!=lado_c){
            System.out.printf("O lado a =  %d\nO lado b = %d\nO lado c = %d\nO triangulo é ESCALENO!!!",lado_a,lado_b,lado_c);
        }
        else{
            System.out.println("Entrada Invalida!!!!");
        }
        scan.close();
    }
}
    
