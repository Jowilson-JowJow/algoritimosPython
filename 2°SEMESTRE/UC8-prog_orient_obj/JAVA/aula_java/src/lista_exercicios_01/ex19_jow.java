//Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
package lista_exercicios_01;

import java.util.Scanner;

public class ex19_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite a primeira nota: ");
        Double nota1 = scan.nextDouble();
        System.out.println("Digite a segunda nota: ");
        Double nota2 = scan.nextDouble();
        System.out.println("Digite a terceira nota: ");
        Double nota3 = scan.nextDouble();
        Double media = (nota1+nota2+2*nota3)/4;
        if (media <6){
            System.out.println("REPROVADO!");
        }
        else{
            System.out.println("APROVADO!");
        }
        scan.close();


    }
    
}
