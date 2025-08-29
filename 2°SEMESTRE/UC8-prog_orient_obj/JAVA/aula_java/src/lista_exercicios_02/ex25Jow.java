//Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3 x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para resolver o problema utilize estrutura de repetição.
package lista_exercicios_02;

import java.util.Scanner;

public class ex25Jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("VAmos calcular potenciação:");
        System.out.println("Digite o base da potencia: ");
        double base = scan.nextDouble();
        System.out.println("Digite o expoente da potencia: ");
        int exp = scan.nextInt();
        int exp_positivo=-exp;
        int i = 0;
        double resultado =1;
        if(exp==0){
            System.out.printf("A potencia do numero %.0f elevado ao expoente %d é igual a %.0f.",base,exp,resultado);  
        }
        else if(exp<0){
            for(i=0;i<exp_positivo;i++){
                resultado*=base;   
            }
            resultado=1/resultado;
            System.out.printf("A potencia do numero %.0f elevado ao expoente %d é igual a %f.",base,exp,resultado);     
        }
        else if(exp>0){
            for(i=0;i<exp;i++){
                resultado*=base;
            }
            System.out.printf("A potencia do numero %.0f elevado ao expoente %d é igual a %.0f.",base,exp,resultado);
        }
        scan.close();
    }
    
}
