//Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, crie um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.
package lista_exercicios_01;

import java.util.Scanner;

public class ex07_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o valor de custo da peça de roupo: R$ ");
        double preco=scan.nextInt();
        
        if(preco<50){
            double venda=preco*1.45;
            System.out.printf("A peça de roupa tem preço de custo de %.2f e sera vendida por %.2f", preco,venda);
        }
        else{
            double venda=preco*1.30;
            System.out.println(venda);
        }
    }
}
