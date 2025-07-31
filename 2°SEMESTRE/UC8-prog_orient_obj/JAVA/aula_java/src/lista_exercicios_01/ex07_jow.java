//Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, crie um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.
package lista_exercicios_01;// Define o pacote onde seu código está (organização de arquivos no Java).

import java.util.Scanner;//Importa a classe Scanner da biblioteca Java, que permite ler dados do teclado.

public class ex07_jow {// Cria a classe pública chamada ex07_jow. Todo programa Java começa com uma classe.


    public static void main(String[] args) {// Esse é o método principal, onde a execução do programa começa.
        Scanner scan = new Scanner(System.in);// Cria um objeto Scanner chamado scan, que será usado para ler entrada do teclado.
        System.out.println("Digite o valor de custo da peça de roupo: R$ ");//Mostra uma mensagem pedindo ao usuário que digite o preço de custo.
        double preco=scan.nextDouble();//Lê um número decimal do teclado e armazena na variável preco.
        
        if(preco<50){
            double venda=preco*1.45;
            System.out.printf("A peça de roupa tem preço de custo de %.2f e sera vendida por %.2f%n", preco,venda);//%n É uma quebra de linha adequada ao sistema operacional, melhor que \n no Java.


        }
        else{
            double venda=preco*1.30;
            System.out.printf("A peça de roupa tem preço de custo de %.2f e sera vendida por %.2f%n", preco,venda);
        }
        scan.close();
    }
}
