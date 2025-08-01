//Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.

package lista_exercicios_01;

import java.util.Scanner;

public class ex16_jow {
    public static void main (String[] args){

        Scanner scan = new Scanner(System.in);
        
        System.out.println("Digite o seu salario: ");
        Double salario = scan.nextDouble();
        
        System.out.println("Digite o valor do emprestimo desejado: ");
        Double emprestimo = scan.nextDouble();
        
        System.out.println("Digite em qauntas parcelas deseja o seu emprestimo: ");
        Double parcelas = scan.nextDouble();
        
        Double valor_parcela= emprestimo/parcelas;
    
        if(valor_parcela>0.2*salario){
            System.out.println("Emprestimo não concedido!!!");
        }
        else if(valor_parcela<=0.2*salario){
            System.out.println("Emprestimo concedido.");
        }
        scan.close();
    }

}
