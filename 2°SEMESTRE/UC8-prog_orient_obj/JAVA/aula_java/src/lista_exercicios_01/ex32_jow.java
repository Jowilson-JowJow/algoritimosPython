//Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
//Especificação Código Preço
//Hot Dog 100 12.00
//X-Salada 102 18.50
//X-BACON 103 25.50
//X-Burguer 104 17.00
//Suco de Laranja 105 9.50
//Refrigerante 106 6.00

package lista_exercicios_01;
import java.util.Scanner;
public class ex32_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        System.out.println("+---------------+-------------+---------+");
        System.out.println("|                CARDÁPIO               |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("| Especificação |    codigo   |  Preço  |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("|    Hot Dog    |     100     |  12,00  |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("|    X-Salada   |     102     |  18,50  |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("|    X-Bacon    |     103     |  25,50  |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("|    X-Burguer  |     104     |  17,00  |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("|Suco de Laranja|     105     |   9,50  |");
        System.out.println("+---------------+-------------+---------+");
        System.out.println("| Refrigerante  |     106     |   6,00  |");
        System.out.println("+---------------+-------------+---------+");

        System.out.println("\nDigite o código do pedido: ");
        int codigo = scan.nextInt();
        
        System.out.println("\nDigite quantas unidades do pedido: ");
        int unidades = scan.nextInt();

        double valor = 0;
        if(codigo==100){
            valor=unidades*12;
            System.out.printf("Seu pedido:\n%d Hot Dog --------------- R$ %.2f",unidades,valor);
        }
        else if( codigo == 102){
            valor=unidades*18.5;
            System.out.printf("Seu pedido:\n%d X-Salada --------------- R$ %.2f",unidades,valor);        
        }
        else if( codigo == 103){
            valor=unidades*25.5;
            System.out.printf("Seu pedido:\n%d X-Bacon --------------- R$ %.2f",unidades,valor);        
        }
        else if( codigo == 104){
            valor=unidades*17;
            System.out.printf("Seu pedido:\n%d X-Burguer --------------- R$ %.2f",unidades,valor);        
        }
        else if( codigo == 105){
            valor=unidades*9.5;
            System.out.printf("Seu pedido:\n%d Suco de Laranja --------------- R$ %.2f",unidades,valor);        
        }
        else if( codigo == 106){
            valor=unidades*6;
            System.out.printf("Seu pedido:\n%d Refrigerante --------------- R$ %.2f",unidades,valor);        
        }
        else{
            System.out.println("Codigo Errado!!!");
        }
        scan.close();


    }
    
}
