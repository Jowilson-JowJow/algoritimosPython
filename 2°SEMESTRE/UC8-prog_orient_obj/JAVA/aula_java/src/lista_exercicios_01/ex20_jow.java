//A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi aprovado. Crie todas as verificações necessárias.

package lista_exercicios_01;

import java.util.Scanner;

public class ex20_jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite a nota do Trabalho de Laboratorio: ");
        Double nota_trabalho = scan.nextDouble();
        System.out.println("Digite a nota da Avaliação Semestral: ");
        Double nota_semestre = scan.nextDouble();
        System.out.println("Digite a nota do Exame Final: ");
        Double nota_exame = scan.nextDouble();
        Double media=(nota_trabalho*2+nota_semestre*3+nota_exame*5)/10;
        if(media<3){
            System.out.printf("A média do aluno é %.2f e o aluno esta REPROVADO!!!",media);
        }
        else if(media<6){
            System.out.printf("A média do aluno é %.2f e o aluno esta de RECUPERAÇÃO!!!",media);
        }
        else{
            System.out.printf("A média do aluno é %2.f e o aluno esta APROVADO!!!",media);
        }
        scan.close();
    }
}
