//Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).
//Preço antigo Percentual de aumento
//até R$ 50 5%
//entre R$ 50 e R$ 100 10%
//acima de R$ 100 15%

package lista_exercicios_01;

import java.util.Scanner;

public class ex33_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o preço atual do produto: ");
        double preco=scan.nextDouble();
        double novo_preco=0;
        if(preco<50){
            novo_preco=preco*1.05;
            System.out.printf("O preço da mercdoria é %.2f e recebera um aumento de 5%%\nAssim seu novo preço será de R$ %.2f",preco,novo_preco);
        }
        else if(preco>=50 && preco<=100){
            novo_preco=preco*1.1;
            System.out.printf("O preço da mercdoria é %.2f e recebera um aumento de 10%%\nAssim seu novo preço será de R$ %.2f",preco,novo_preco);
        }
        else if(preco>100){
            novo_preco=preco*1.15;
            System.out.printf("O preço da mercdoria é %.2f e recebera um aumento de 15%%\nAssim seu novo preço será de R$ %.2f",preco,novo_preco);
        }
        scan.close();

    }
    
}
