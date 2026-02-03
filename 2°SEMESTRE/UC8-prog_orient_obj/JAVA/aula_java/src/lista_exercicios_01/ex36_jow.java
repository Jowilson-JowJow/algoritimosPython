// //O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
// CUSTO DE FÁBRICA % DO DISTRIBUIDOR % DOS IMPOSTOS
// até R$12.000,00 5 isento
// entre R$12.000,00 e 25.000,00 10 15
// acima de R$25.000,00 15 20
package lista_exercicios_01;

import java.util.Scanner;

public class ex36_jow {;

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o preço de custo do automoveL: ");
        double custo=scan.nextDouble();
        double preco =0;
        if (custo<12000){
            preco=custo + custo*0.05;
            System.out.println("O preço de custo do veiculo é R$ "+custo+" E o preço de venda é de R$ "+preco);
        }
        else if(custo>=12000 && custo<=25000){
            preco=custo+custo*0.1+custo*0.15;
            System.out.println("O preço de custo do veiculo é R$ "+custo+" E o preço de venda é de R$ "+preco);
        }   
        else if(custo>25000){
            preco=custo+custo*0.15+custo*0.2;
            System.out.println("O preço de custo do veiculo é R$ "+custo+" E o preço de venda é de R$ "+preco);
        } 
        scan.close();


    }
    
}
