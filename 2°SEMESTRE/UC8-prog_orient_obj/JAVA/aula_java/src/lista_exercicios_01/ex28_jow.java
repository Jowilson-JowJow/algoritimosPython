//Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
//• Ter pelo menos 65 anos,
//• Ou ter trabalhado pelo menos 30 anos,
//• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
package lista_exercicios_01;
import java.util.Scanner;
public class ex28_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner (System.in);
        System.out.println("Digite a sua idade: ");
        int idade = scan.nextInt();
        System.out.println("Digite seu tempo de contribuição: ");
        int tempo = scan.nextInt();
        if(idade>=65 && tempo>=30){
            System.out.println("Você ja pode aposentar!!!");
        }
        else if(idade>=60 && tempo>=25){
            System.out.println("Você ja pode aposentar!!!");
        }
        else{
            System.out.println("Você NÃO pode aposentar!!!");
        }
        scan.close();
    }
    
}
