//Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o chute e menor ou maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
package lista_exercicios_02; 
import java.util.Scanner;
import java.util.Random;

public class ex39Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        Random rate = new Random();
        int numero = rate.nextInt(101);
        System.out.println("Vamos brincar?\nEu acabei de escolher um numero entre 0 e 100, VOCÊ consegue descobrir qual foi esse numero escolhido?");
        System.out.println("Tente adivinhar, Qual foi o numero escolhido? ");
        int num_digitado=scan.nextInt();
        while(true){
            if(num_digitado==numero){
                System.out.println("PARABÉNS!!!\nVocê acertou o numero!");
                break;
            }
            else{
                if(num_digitado<numero){
                    System.out.println("O numero digitado é menor que o numero escolhido: \nTente de novo: ");
                    num_digitado=scan.nextInt();
                }
                else if(num_digitado>numero){
                    System.out.println("O numero digitado é maior que o numero escolhido:\nTente de novo: ");
                    num_digitado=scan.nextInt();
                }
            }
        }
        scan.close();
    }    
}
