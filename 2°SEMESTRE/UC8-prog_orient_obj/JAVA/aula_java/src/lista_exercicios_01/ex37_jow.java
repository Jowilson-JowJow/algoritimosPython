//Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
// IMC Classificação
// < 18,5 Abaixo do Peso
// 18,6 - 24,9 Saudável
// 25,0 - 29,9 Peso em excesso
// 30,0 - 34,9 Obesidade Grau I
// 35,0 - 39,9 Obesidade Grau II (severa)
// ≥ 40,0 Obesidade Grau III (mórbida)
package lista_exercicios_01;

import java.util.Scanner;

public class ex37_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Vamos calcular o seu IMC.\n");
        System.out.println("Digite seu Peso:\n");
        double peso = scan.nextDouble();
        System.out.println("Digite sua Altura:\n");
        double altura = scan.nextDouble();
        double imc = peso/(altura*altura);
        if (imc<18.6){
            System.out.println("Seu IMC é "+ imc+ "\nAbaixo Peso");
        }
        else if(imc>=18.6 && imc<25){
            System.out.println("Seu IMC é "+ imc+ "\nSaudavel");
        }
        else if(imc>=25 && imc<30){
            System.out.println("Seu IMC é "+ imc+ "\nPeso em excesso");
        }
        else if(imc>=30 && imc<35){
            System.out.println("Seu IMC é "+ imc+ "\nObesidade grau I");
        }
        else if(imc>=35 && imc<40){
            System.out.println("Seu IMC é "+ imc+ "\nObesidade grau II (severa)");
        }
        else if(imc>=40){
            System.out.println("Seu IMC é "+ imc+ "\nObesidade grau III (mórbida)");
        }
        scan.close();
    }
    
}
